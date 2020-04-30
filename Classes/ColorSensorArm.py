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
        self.Speed = 500
        self.StopAction = 'hold'
        
        self.RunForever()

        self.WaitUntilStalled()
        self.MotorReset()

    #
    # PutAway
    # Put the sensor arm away of the cube
    def PutAway(self):
        self.Position = 0
        self.RampDown = 0
        self.RampUp = 0
        self.Speed = 1200
        self.StopAction = 'hold'

        self.RunToAbsolutePosition()

        self.WaitWhileRunning()
        self.MotorOff()

    #
    # PutHalfAway
    # Put the sensor arm away of the cube
    def PutHalfAway(self):
        self.Position = -400
        self.RampDown = 0
        self.RampUp = 0
        self.Speed = 1200
        self.StopAction = 'hold'

        self.RunToAbsolutePosition()

        self.WaitWhileRunning()
        self.MotorOff()

    #
    # TakeOutCorner
    # Take out the arm to the cube corner in front of the sensor
    def TakeOutCorner(self):
        self.Position = -580
        self.RampDown = 0
        self.RampUp = 0
        self.Speed = 300
        self.StopAction = 'hold'

        self.RunToAbsolutePosition()

        self.WaitWhileRunning()
        self.MotorOff()

    #
    # TakeOutEdge
    # Take out the arm to the cube edge in front of the sensor
    def TakeOutEdge(self):
        self.Position = -650
        self.RampDown = 0
        self.RampUp = 0
        self.Speed = 300
        self.StopAction = 'hold'

        self.RunToAbsolutePosition()

        self.WaitWhileRunning()
        self.MotorOff()

    #
    # TakeOutMiddle
    # Take out the arm to the middle of the cube top face
    def TakeOutMiddle(self):
        self.Position = -750
        self.RampDown = 0
        self.RampUp = 0
        self.Speed = 1200
        self.StopAction = 'hold'

        self.RunToAbsolutePosition()
        
        self.WaitWhileRunning()
        self.MotorOff()
