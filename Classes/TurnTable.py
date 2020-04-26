# EV3
from ev3dev2.motor import LargeMotor, SpeedDPS

class TurnTable:
    Motor = None

    #
    # Init
    # Initialize the motor
    def __init__(self, MotorPort):
        self.Motor = LargeMotor(address = MotorPort)

        # Init the motor
        self.__SetStopAction(Action = 'hold')
        self.InitPosition()

    ###################
    # Exposed Methods #
    ###################

    #
    # HalfQuarterRotate
    # Rotate the platform for a half quarter rotation
    def HalfQuarterRotate(self):
        self.__MotorOnToPosition(Speed = 200, Position = 100)

    #
    # InitPosition
    # Initialize the arm position
    def InitPosition(self):
        self.__MotorOff(Reset = True)

    #
    # IsTurning
    # Expose the motor state: true if the table is turning
    def IsTurning(self):
        return True if 'running' in self.__GetState() else False

    #
    # QuarterRotate
    # Rotate the platform for a quarter rotation
    def QuarterRotate(self):
        self.__MotorOnToPosition(Speed = 200, Position = 275)

    #
    # Stop
    # Stop the motor
    def Stop(self):
        self.__MotorOff()

    #
    # TurnForDegrees
    # Turn the table for given degrees
    def TurnForDegrees(self, Degrees):
        self.__MotorOnForDegress(Speed = 200, Degrees = Degrees)
        self.__MotorOff()

    #
    # TurnForever
    # Turn the table for ever
    def TurnForever(self, Block, Clockwize = True):
        Speed = 200
        if not Clockwize:
            Speed = -200

        self.__MotorOnForever(Speed = Speed, Block = Block)
        if Block:
            self.__MotorOff()

    ###################
    # Private Methods #
    ###################

    #
    # GetState
    # Return the current states list of the motor
    def __GetState(self):
        return self.Motor.state

    #
    # MotorOff
    # Shutdown the motor 
    def __MotorOff(self, Reset = False):
        self.Motor.stop()
        if Reset:
            self.Motor.reset()
            self.Motor.position = 0
            self.__SetStopAction(Action = 'hold')

    #
    # MotorOnForDegress
    # Put the motor on to the given position at the given speed
    def __MotorOnForDegress(self, Speed, Degrees):
        self.Motor.on_for_degrees(speed = SpeedDPS(Speed), degrees = Degrees, block = True)

    #
    # MotorOnForever
    # Put the motor on forever at given speed
    def __MotorOnForever(self, Speed, Block):
        self.Motor.on(speed = SpeedDPS(Speed), block = Block)

    #
    # MotorOnToPosition
    # Put the motor on to the given position at the given speed
    def __MotorOnToPosition(self, Speed, Position):
        self.Motor.on_to_position(speed = SpeedDPS(Speed), position = Position, block = True)

    #
    # SetStopAction
    # Define the stop action of the motor
    def __SetStopAction(self, Action):
        self.Motor.stop_action = Action