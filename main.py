#!/usr/bin/env python3

# EV3 Motors
from ev3dev2.motor import OUTPUT_A as OutPortA
from ev3dev2.motor import OUTPUT_B as OutPortB
from ev3dev2.motor import OUTPUT_C as OutPortC

# EV3 Sensors
from ev3dev2.sensor import INPUT_1 as InPort1
from ev3dev2.sensor import INPUT_2 as InPort2

# Robot Classes
from Classes.Robot.BrickButton import BrickButton
from Classes.Robot.BrickVoice import BrickVoice
from Classes.Robot.ColorSensorArm import ColorSensorArm
from Classes.Robot.ColorSensorUnit import ColorSensorUnit
from Classes.Robot.RedEyes import RedEyes
from Classes.Robot.ShufflerArm import ShufflerArm
from Classes.Robot.TurnTable import TurnTable

# Rubik Classes
from Classes.Rubik.Cube import Cube

# Python
from time import sleep as Sleep

class CubeSolver:
    CubeMiddleSquareIndexes = [ 5, 32, 50, 23, 14, 41 ]
    CubeScannedFaces = 0
    CubeSquareColors = {}
    CubeSquareIndex = 0
    CubeSquareScanOrder = [
        5, 3, 2, 1, 4, 7, 8, 9, 6,
        32, 36, 33, 30, 29, 28, 31, 34, 35,
        50, 52, 53, 54, 51, 48, 47, 46, 49,
        23, 19, 22, 25, 26, 27, 24, 21, 20,
        14, 16, 17, 18, 15, 12, 11, 10, 13,
        41, 43, 44, 45, 42, 39, 38, 37, 40
    ]
    Ev3Button = None
    Ev3ColorSensorArm = None
    Ev3ColorSensorUnit = None
    Ev3RedEyes = None
    Ev3ShufflerArm = None
    Ev3Speaker = None
    Ev3TurnTable = None

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
        self.Ev3Button.ButtonLeftCallbackFunc = self.Ev3TurnTable.TurnToRelativePosition
        self.Ev3Button.ButtonLeftCallbackArgs['RelativePosition'] = -1
        self.Ev3Button.ButtonRightCallbackFunc = self.Ev3TurnTable.TurnToRelativePosition
        self.Ev3Button.ButtonRightCallbackArgs['RelativePosition'] = 1

        while True:
            if self.Ev3Button.Button.enter:
                break

            self.Ev3Button.Button.process()
            Sleep(.01)

        self.Ev3TurnTable.ResetTable()

        # Adjust the cube initial position once the table is correctly initialized
        self.Ev3ShufflerArm.PutArmDown()
        Sleep(.5)
        self.Ev3ShufflerArm.PutArmUp()

    #
    # Scan
    # Scan the cube
    def Scan(self):
        self.CubeScannedFaces = 0
        for CubeFaceIndex in range(6):
            self.__ScanCubeTopFace()
            self.CubeScannedFaces += 1

            if self.CubeScannedFaces == 3:
                self.Ev3TurnTable.QuarterTurn(Clockwise = False)
                self.Ev3ShufflerArm.FlipCube()
            elif self.CubeScannedFaces == 4:
                self.Ev3TurnTable.QuarterTurn()
                self.Ev3ShufflerArm.FlipCube()
            elif self.CubeScannedFaces == 6:
                self.Ev3TurnTable.QuarterTurn(Clockwise = False)
                self.Ev3ShufflerArm.FlipCube()
                self.Ev3TurnTable.QuarterTurn()
                self.Ev3ShufflerArm.PutArmDown()
                Sleep(.5)
                self.Ev3ShufflerArm.PutArmUp()
            else:
                self.Ev3ShufflerArm.FlipCube()

    ###################
    # Private Methods #
    ###################
    #
    # ScanCubeTopFace
    # Scan the top face of the cube
    def __ScanCubeTopFace(self):
        if self.Ev3ShufflerArm.GetArmPosition() > 35:
            self.Ev3ShufflerArm.PutArmUp()

        SquareCounter = 0

        self.Ev3ColorSensorArm.TakeOutMiddle()
        self.CubeSquareColors[self.CubeSquareScanOrder[self.CubeSquareIndex]] = self.Ev3ColorSensorUnit.GetRgbColor()

        self.CubeSquareIndex += 1
        self.Ev3ColorSensorArm.TakeOutCorner()
        SquareCounter += 1

        # Full turn of the table, but do not block so the process can continue
        self.Ev3TurnTable.FullTurnFromPositionZero(Block = False)

        while self.Ev3TurnTable.IsTableTurning():
            CurrentPosition = self.Ev3TurnTable.GetTablePosition()
            
            if CurrentPosition >= (SquareCounter * 135) - 5:
                self.CubeSquareColors[self.CubeSquareScanOrder[self.CubeSquareIndex]] = self.Ev3ColorSensorUnit.GetRgbColor()
                
                self.CubeSquareIndex += 1
                SquareCounter += 1

                if SquareCounter == 9:
                    if self.CubeScannedFaces == 5:
                        self.Ev3ColorSensorArm.PutAway()
                    else:
                        self.Ev3ColorSensorArm.PutHalfAway()
                elif SquareCounter % 2:
                    self.Ev3ColorSensorArm.TakeOutCorner()
                else:
                    self.Ev3ColorSensorArm.TakeOutEdge()

            if SquareCounter == 9:
                self.Ev3TurnTable.StopTable()

################
# Main Program #
################
Solver = CubeSolver()
Solver.AdjustTurnTable()
Solver.Scan()

RubikCube = Cube()
Result = RubikCube.ImportScannedData(ScannedData = Solver.CubeSquareColors)
RubikCube.PrintCube()
