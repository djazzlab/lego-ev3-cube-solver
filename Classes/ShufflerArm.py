# EV3
from ev3dev2.motor import LargeMotor, SpeedDPS

class ShufflerArm:
    Motor = None

    #
    # Init
    # Initialize face switcher arm
    def __init__(self, MotorPort):
        self.Motor = LargeMotor(address = MotorPort)
        
        # Init the motor
        self.__SetStopAction(Action = 'hold')
        self.__InitPosition()

    ###################
    # Exposed Methods #
    ###################

    #
    # FlipFace
    # Move the arm down on the cube and start face flipping
    def FlipFace(self):
        self.__MotorOnToPosition(Speed = 300, Position = 200)
        self.__MotorOff()
        self.PutAway()

    #
    # PutArmDown
    # Move the arm down to the cube but do not flip the top face
    # Useful to reset the cube location on the turn table
    def PutArmDown(self):
        self.__MotorOnToPosition(Speed = 300, Position = 100)
        self.__MotorOff()

    #
    # PutAway
    # Move to the initial position
    def PutAway(self):
        self.__MotorOnToPosition(Speed = 300, Position = 0)
        self.__MotorOff()

    ###################
    # Private Methods #
    ###################

    #
    # InitPosition
    # Initialize the arm position
    def __InitPosition(self):
        self.__MotorOnForever(Speed = -130)
        self.__MotorOff(Reset = True)

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
    # MotorOnForever
    # Put the motor on forever at given speed
    def __MotorOnForever(self, Speed):
        self.Motor.on(speed = SpeedDPS(Speed), block = True)

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