#!/usr/bin/env python3

# EV3 Motors
from ev3dev2.motor import OUTPUT_A as OutPortA
from ev3dev2.motor import OUTPUT_B as OutPortB
from ev3dev2.motor import OUTPUT_C as OutPortC

# EV3 Sensors
from ev3dev2.sensor import INPUT_1 as InPort1
from ev3dev2.sensor import INPUT_2 as InPort2

# Local resources
from Classes.BrickButton import BrickButton
from Classes.BrickVoice import BrickVoice
from Classes.ColorSensorArm import ColorSensorArm
from Classes.ColorSensorUnit import ColorSensorUnit
from Classes.RedEyes import RedEyes
from Classes.ShufflerArm import ShufflerArm
from Classes.TurnTable import TurnTable

# Python
from time import sleep as Sleep

class CubeSolver:
    CubeSquareColors = {}
    CubeMiddleSquareIndexes = [ 5, 32, 50, 14, 23, 41 ]
    Ev3Button = None
    Ev3ColorSensorArm = None
    Ev3ColorSensorUnit = None
    Ev3RedEyes = None
    Ev3ShufflerArm = None
    Ev3Speaker = None
    Ev3TurnTable = None
    FaceSquareIndexTransformations = [ 0, -2, -1, -1, 3, 3, 1, 1, -3 ]

    ##########################
    # Initialization Methods #
    ##########################
    def __init__(self):
        # Speaker
        self.Ev3Speaker = BrickVoice()

        self.Ev3Speaker.Speak(Message = 'Welcome to the E V 3 Cube Solver machine!')
        self.Ev3Speaker.Speak(Message = 'Initialization of the robot...')

        # Configure the brick buttons
        self.Ev3Button = BrickButton()

        # Configure the EV3 cube face flipper arm on output port A
        self.Ev3ShufflerArm = ShufflerArm(MotorPort = OutPortA)
        self.Ev3ShufflerArm.InitArmPosition()

        # Configure the EV3 rotation platform on output port B
        self.Ev3TurnTable = TurnTable(MotorPort = OutPortB)

        # Configure the EC3 infrared sensor on input port 1
        self.Ev3RedEyes = RedEyes(SensorPort = InPort1)
        self.Ev3RedEyes.InitSensor()

        # Configure the EV3 color sensor arm on output port C
        self.Ev3ColorSensorArm = ColorSensorArm(MotorPort = OutPortC)
        self.Ev3ColorSensorArm.InitArmPosition()

        # Configure the EV3 color sensor device on input port 2
        self.Ev3ColorSensorUnit = ColorSensorUnit(SensorPort = InPort2)
        self.Ev3ColorSensorUnit.InitSensor()

    ###################
    # Exposed Methods #
    ###################
    #
    # AdjustTurnTable
    # Allows to rotate the turn table to the initial perpendicular position
    def AdjustTurnTable(self):
        # Align the platform using the brick buttons
        self.Ev3Speaker.Speak(Message = 'Please align the turn table using the left and right brick buttons, press enter when you are good!')
        # Rotation platform calibration
        # +/- 3 degrees because the ratio between the wheels is 3 (12 and 36 pins)
        # So to rotate the big wheel for 1 degree, the small one (and therefor the motor) has to rotate for 3 degrees
        self.Ev3Button.ButtonLeftCallbackFunc = self.Ev3TurnTable.TurnForRelativePosition
        self.Ev3Button.ButtonLeftCallbackArgs['RelativePosition'] = -1
        self.Ev3Button.ButtonRightCallbackFunc = self.Ev3TurnTable.TurnForRelativePosition
        self.Ev3Button.ButtonRightCallbackArgs['RelativePosition'] = 1

        while True:
            if self.Ev3Button.Button.enter:
                break

            self.Ev3Button.Button.process()
            Sleep(.01)

        self.Ev3TurnTable.StopTable(Reset = True)

        # Adjust the cube initial position once the table is correctly initialized
        self.Ev3ShufflerArm.PutArmDown()
        Sleep(.5)
        self.Ev3ShufflerArm.PutArmUp()

    #
    # Scan
    # Scan the cube
    def Scan(self):
        for CubeMiddleSquareIndex in self.CubeMiddleSquareIndexes:
            self.__ScanCubeTopFace(CubeSquareIndex = CubeMiddleSquareIndex)
            #self.Ev3ShufflerArm.FlipCube()

    ###################
    # Private Methods #
    ###################
    #
    # ScanCubeTopFace
    # Scan the top face of the cube
    def __ScanCubeTopFace(self, CubeSquareIndex):
        if self.Ev3ShufflerArm.GetArmPosition() > 35:
            self.Ev3ShufflerArm.PutArmUp()

        SquareCounter = 0

        self.Ev3ColorSensorArm.TakeOutMiddle()
        self.CubeSquareColors[CubeSquareIndex] = self.Ev3ColorSensorUnit.GetRGBColor()

        self.Ev3ColorSensorArm.TakeOutCorner()
        SquareCounter += 1

        # Full turn of the table, but do not block so the process can continue
        self.Ev3TurnTable.FullTurn(Block = False)

        while self.Ev3TurnTable.IsTableTurning():
            CurrentPosition = self.Ev3TurnTable.GetTablePosition()
            
            if CurrentPosition >= (SquareCounter * 135) - 5:
                CubeSquareIndex = CubeSquareIndex + self.FaceSquareIndexTransformations[SquareCounter]
                self.CubeSquareColors[CubeSquareIndex] = self.Ev3ColorSensorUnit.GetRGBColor()
                
                SquareCounter += 1

                if SquareCounter == 9:
                    self.Ev3TurnTable.StopTable(Reset = True)
                    self.Ev3ColorSensorArm.PutHalfAway()
                elif SquareCounter % 2:
                    self.Ev3ColorSensorArm.TakeOutCorner()
                else:
                    self.Ev3ColorSensorArm.TakeOutEdge()

################
# Main Program #
################
Solver = CubeSolver()
Solver.AdjustTurnTable()
Solver.Scan()
