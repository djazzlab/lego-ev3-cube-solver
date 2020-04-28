class Ev3Motor:
    __Motor = None

    #
    # Init
    # Initialize the motor
    def __init__(self, Motor):
        self.__Motor = Motor

    #
    # GetMotorPosition
    # Returns the motor position
    def GetMotorPosition(self, SP = False):
        if SP:
            return self.__Motor.position_sp
        return self.__Motor.position

    #
    # GetPolarity
    # Returns motor polarity
    def GetPolarity(self):
        return self.__Motor.polarity

    #
    # GetState
    # Return the current states list of the motor
    def GetState(self):
        return self.__Motor.state

    #
    # MotorOff
    # Shutdown the motor 
    def MotorOff(self, Reset = False):
        self.__Motor.stop()
        if Reset:
            self.__Motor.reset()

    #
    # SetPolarity
    # Set motor polarity
    def SetPolarity(self, Polarity):
        self.__Motor.polarity = Polarity

    #
    # SetPosition
    # Set motor position
    def SetPosition(self, Position, SP = False):
        if SP:
            self.__Motor.position_sp = Position
        else:
            self.__Motor.position = Position

    #
    # SetRamps
    # Set ramp up and ramp down setpoints
    def SetRamps(self, Up, Down):
        self.__Motor.ramp_up_sp = Up
        self.__Motor.ramp_down_sp = Down

    #
    # SetRunForever
    # Run the motor until another command is sent
    def SetRunForever(self):
        self.__Motor.command = self.__Motor.COMMAND_RUN_FOREVER

    #
    # SetRunToAbsolutePosition
    # Run to a position relative to the current position value
    def SetRunToAbsolutePosition(self):
        self.__Motor.command = self.__Motor.COMMAND_RUN_TO_ABS_POS

    #
    # SetRunToRelativePosition
    # Run to a position relative to the current position value
    def SetRunToRelativePosition(self):
        self.__Motor.command = self.__Motor.COMMAND_RUN_TO_REL_POS

    #
    # SetSpeed
    # Set the speed_sp value
    def SetSpeed(self, Speed, SP = False):
        if SP:
            self.__Motor.speed_sp = Speed
        else:
            self.__Motor.speed = Speed

    #
    # SetStopActionBrake
    # Power will be removed from the motor and a passive electrical load will be placed on the motor
    def SetStopActionBrake(self):
        self.__Motor.stop_action = self.__Motor.STOP_ACTION_BRAKE

    #
    # SetStopActionHold
    # Actively try to hold the motor at the current position
    def SetStopActionHold(self):
        self.__Motor.stop_action = self.__Motor.STOP_ACTION_HOLD

    #
    # WaitUntilStalled
    # Blocks until the motor is not turning when it should be
    def WaitUntilStalled(self):
        self.__Motor.wait_until(self.__Motor.STATE_STALLED)

    #
    # WaitWhileRunning
    # Blocks while the motor is running
    def WaitWhileRunning(self):
        self.__Motor.wait_while(self.__Motor.STATE_RUNNING)