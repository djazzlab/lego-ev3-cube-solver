# EV3
from ev3dev2.motor import LargeMotor

# Local resources
from Classes.Ev3Motor import Ev3Motor

class TurnTable(Ev3Motor):
    #
    # Init
    # Initialize the motor
    def __init__(self, MotorPort):
        super().__init__(Motor = LargeMotor(address = MotorPort))

    #
    # FullTurn
    # Turn the table for one full turn
    # As the gears ratio of the table is 1:3, then the motor has to turn for 360*3=1080
    def FullTurn(self, Block = True):
        self.MotorOff(Reset = True)
        self.SetStopActionHold()
        self.SetRamps(Up = 0, Down = 0)
        self.SetSpeed(Speed = 400, SP = True)
        self.SetPosition(Position = 1080, SP = True)
        self.SetRunToRelativePosition()

        if Block:
            self.WaitWhileRunning()
            self.MotorOff(Reset = True)

    #
    # GetTablePosition
    # Return the current position of the motor
    def GetTablePosition(self):
        return self.GetMotorPosition(SP = True)

    #
    # IsTableTurning
    # Expose the motor state: true if the table is turning
    def IsTableTurning(self):
        return True if 'running' in self.GetState() else False

    #
    # Stop
    # Stop the motor
    def StopTable(self, Reset = False):
        self.MotorOff(Reset = Reset)
        if Reset:
            self.SetPosition(Position = 0, SP = True)
            self.SetStopActionHold()

    #
    # TurnForRelativePosition
    # Turn the table to a relative position to the current position
    def TurnForRelativePosition(self, RelativePosition, Block = True):
        self.SetStopActionHold()
        self.SetRamps(Up = 0, Down = 0)
        self.SetSpeed(Speed = 400, SP = True)
        self.SetPosition(Position = RelativePosition, SP = True)
        self.SetRunToRelativePosition()

        if Block:
            self.WaitWhileRunning()
            self.MotorOff()
