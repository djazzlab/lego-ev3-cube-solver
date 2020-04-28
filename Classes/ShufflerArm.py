# EV3
from ev3dev2.motor import LargeMotor

# Local resources
from Classes.Ev3Motor import Ev3Motor

class ShufflerArm(Ev3Motor):
    __HoldCubePosition = 85

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
        if (Position <= self.__HoldCubePosition - 10) or (Position >= self.__HoldCubePosition + 10):
            self.PutArmDown()

        # Flipping
        self.SetStopActionBrake()
        self.SetRamps(Up = 200, Down = 0)
        self.SetSpeed(Speed = 400, SP = True)
        self.SetPosition(Position = 180, SP = True)
        self.SetRunToAbsolutePosition()
        self.WaitWhileRunning()
        self.MotorOff()
        
        # Put the cube at the starting position before the flip
        self.PutArmUp()

    #
    # GetArmPosition
    # Return the current position of the motor
    def GetArmPosition(self):
        return self.GetMotorPosition(SP = True)

    #
    # InitArmPosition
    # Initialize the arm position
    def InitArmPosition(self):
        self.SetStopActionBrake()
        self.SetRamps(Up = 0, Down = 0)
        self.SetSpeed(Speed = -130, SP = True)
        self.SetRunForever()
        self.WaitUntilStalled()
        self.MotorOff(Reset = True)
        self.SetPosition(Position = 0, SP = True)

    #
    # PutArmDown
    # Move the arm down to the cube but do not flip the top face
    # Useful to reset the cube location on the turn table
    def PutArmDown(self):
        self.SetStopActionBrake()
        self.SetRamps(Up = 0, Down = 0)
        self.SetSpeed(Speed = 400, SP = True)
        self.SetPosition(Position = self.__HoldCubePosition, SP = True)
        self.SetRunToAbsolutePosition()
        self.WaitWhileRunning()
        self.MotorOff()

    #
    # PutArmUp
    # Move the arm up so the cube can be scanned or fully rotated
    def PutArmUp(self):
        self.SetStopActionBrake()
        self.SetRamps(Up = 0, Down = 0)
        self.SetSpeed(Speed = 400, SP = True)
        self.SetPosition(Position = 0, SP = True)
        self.SetRunToAbsolutePosition()
        self.WaitWhileRunning()
        self.MotorOff()
