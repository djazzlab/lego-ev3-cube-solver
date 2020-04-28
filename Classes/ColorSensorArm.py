# EV3
from ev3dev2.motor import MediumMotor

# Local resources
from Classes.Ev3Motor import Ev3Motor

class ColorSensorArm(Ev3Motor):
    #
    # Init
    # Initialize the motor
    def __init__(self, MotorPort):
        super().__init__(Motor = MediumMotor(address = MotorPort))

    #
    # InitArmPosition
    # Initialize the arm position
    def InitArmPosition(self):
        self.SetStopActionBrake()
        self.SetSpeed(Speed = 500, SP = True)
        self.SetRunForever()
        self.WaitUntilStalled()
        self.MotorOff(Reset = True)
        self.SetPosition(Position = 0, SP = True)

    #
    # PutAway
    # Put the sensor arm away of the cube
    def PutAway(self):
        self.SetStopActionHold()
        self.SetRamps(Up = 0, Down = 0)
        self.SetSpeed(Speed = 1200, SP = True)
        self.SetPosition(Position = 0, SP = True)
        self.SetRunToAbsolutePosition()
        self.WaitWhileRunning()
        self.MotorOff()

    #
    # PutHalfAway
    # Put the sensor arm away of the cube
    def PutHalfAway(self):
        self.SetStopActionHold()
        self.SetRamps(Up = 0, Down = 0)
        self.SetSpeed(Speed = 1200, SP = True)
        self.SetPosition(Position = -400, SP = True)
        self.SetRunToAbsolutePosition()
        self.WaitWhileRunning()
        self.MotorOff()

    #
    # TakeOutCorner
    # Take out the arm to the cube corner in front of the sensor
    def TakeOutCorner(self):
        self.SetStopActionHold()
        self.SetRamps(Up = 0, Down = 0)
        self.SetSpeed(Speed = 1200, SP = True)
        self.SetPosition(Position = -580, SP = True)
        self.SetRunToAbsolutePosition()
        self.WaitWhileRunning()
        self.MotorOff()

    #
    # TakeOutEdge
    # Take out the arm to the cube edge in front of the sensor
    def TakeOutEdge(self):
        self.SetStopActionHold()
        self.SetRamps(Up = 0, Down = 0)
        self.SetSpeed(Speed = 1200, SP = True)
        self.SetPosition(Position = -650, SP = True)
        self.SetRunToAbsolutePosition()
        self.WaitWhileRunning()
        self.MotorOff()

    #
    # TakeOutMiddle
    # Take out the arm to the middle of the cube top face
    def TakeOutMiddle(self):
        self.SetStopActionHold()
        self.SetRamps(Up = 0, Down = 0)
        self.SetSpeed(Speed = 1200, SP = True)
        self.SetPosition(Position = -750, SP = True)
        self.SetRunToAbsolutePosition()
        self.WaitWhileRunning()
        self.MotorOff()
