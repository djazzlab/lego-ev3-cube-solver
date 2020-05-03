# EV3
from ev3dev2.motor import LargeMotor

# Local resources
from Classes.Robot.Ev3Motor import Ev3Motor

class TurnTable(Ev3Motor):
    #
    # Init
    # Initialize the motor
    def __init__(self, MotorPort):
        super().__init__(Motor = LargeMotor(address = MotorPort))

    #
    # FullTurnFromPositionZero
    # Turn the table for one full turn from position 0
    # As the gears ratio of the table is 1:3, then the motor has to turn for 360*3=1080
    def FullTurnFromPositionZero(self, Block = True):
        self.Position = 1080
        self.RampDown = 0
        self.RampUp = 0
        self.Speed = 400
        self.StopAction = 'hold'

        self.RunToRelativePosition()

        if Block:
            self.WaitWhileRunning()
            self.MotorReset()

    #
    # GetTablePosition
    # Return the current position of the motor
    def GetTablePosition(self):
        return self.GetMotorPosition()

    #
    # IsTableTurning
    # Expose the motor state: true if the table is turning
    def IsTableTurning(self):
        return True if 'running' in self.GetState() else False

    #
    # QuarterTurn
    # Turn the table for one quarter
    def QuarterTurn(self, Clockwise = True):
        self.Position = 270 if Clockwise else -270
        self.RampDown = 300
        self.RampUp = 0
        self.Speed = 600
        self.StopAction = 'hold'

        self.RunToRelativePosition()
        
        self.WaitWhileRunning()
        self.MotorOff()

    #
    # ResetTable
    # Reset the table motor
    def ResetTable(self):
        self.MotorReset()
        
    #
    # StopTable
    # Stop the table motor
    def StopTable(self, Reset = False):
        self.MotorOff()
        if Reset:
            self.MotorReset()

    #
    # TurnToRelativePosition
    # Turn the table to a relative position to the current position
    def TurnToRelativePosition(self, RelativePosition, Block = True):
        self.Position = RelativePosition
        self.RampDown = 0
        self.RampUp = 0
        self.Speed = 400
        self.StopAction = 'hold'

        self.RunToRelativePosition()

        if Block:
            self.WaitWhileRunning()
            self.MotorOff()
