# EV3
from ev3dev2.motor import LargeMotor

# Local resources
from Classes.Ev3Motor import Ev3Motor

# Python
from time import sleep as Sleep

class ShufflerArm(Ev3Motor):
    #
    # Init
    # Initialize face switcher arm
    def __init__(self, MotorPort):
        super().__init__(Motor = LargeMotor(address = MotorPort))

    #
    # FlipCube
    # Move the arm down on the cube and start face flipping
    def FlipCube(self):
        Position = self.GetArmPosition()

        # Make sure the cube is always at the same position before flipping it
        if (Position <= 75) or (Position >= 95):
            self.PutArmDown()

        # Flipping
        self.Position = 180
        self.RampDown = 0
        self.RampUp = 200
        self.Speed = 400
        self.StopAction = 'hold'

        self.RunToAbsolutePosition()
        
        self.WaitWhileRunning()
        self.MotorOff()

        # Sleep 0.5 secondes
        Sleep(.5)
        
        # Put the cube at the starting position before the flip
        self.PutArmUp()

    #
    # GetArmPosition
    # Return the current position of the motor
    def GetArmPosition(self):
        return self.GetMotorPosition()

    #
    # InitArmPosition
    # Initialize the arm position
    def InitArmPosition(self):
        self.Position = 85
        self.RampDown = 0
        self.RampUp = 0
        self.Speed = -130
        self.StopAction = 'hold'

        self.RunForever()
        
        self.WaitUntilStalled()
        self.MotorReset()

    #
    # PutArmDown
    # Move the arm down to the cube but do not flip the top face
    # Useful to reset the cube location on the turn table
    def PutArmDown(self):
        self.Position = 85
        self.RampDown = 0
        self.RampUp = 0
        self.Speed = 200
        self.StopAction = 'hold'
        
        self.RunToAbsolutePosition()

        self.WaitWhileRunning()
        self.MotorOff()

    #
    # PutArmUp
    # Move the arm up so the cube can be scanned or fully rotated
    def PutArmUp(self):
        self.Position = 0
        self.RampDown = 0
        self.RampUp = 0
        self.Speed = 200
        self.StopAction = 'hold'

        self.RunToAbsolutePosition()

        self.WaitWhileRunning()
        self.MotorOff()
