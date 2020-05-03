class Ev3Sensor:
    __Sensor = None

    #
    # Init
    # Initialize the sensor
    def __init__(self, Sensor):
        self.__Sensor = Sensor

    ##################
    # Common Methods #
    ##################
    #
    # SetSensorMode
    # Register the mode Mode to the sensor
    def SetSensorMode(self, Mode):
        if self.__Sensor.mode != Mode:
            self.__Sensor.mode = Mode

    #################
    # Color Sensors #
    #################
    #
    # SetModeRGBRAW
    # Register the mode IR-PROX for the sensor
    def SetModeRGBRAW(self):
        self.SetSensorMode(Mode = self.__Sensor.MODE_RGB_RAW)

    #
    # GetRgbColor
    # Return a tuple of the rgb color code detected by the sensor
    def GetRgbColor(self):
        return self.__Sensor.rgb

    ####################
    # Infrared Sensors #
    ####################
    #
    # GetProximity
    # Return the distance between the eyes and the front object
    def GetProximity(self):
        return self.__Sensor.proximity

    #
    # SetModeIRProx
    # Register the mode IR-PROX for the sensor
    def SetModeIRProx(self):
        self.SetSensorMode(Mode = self.__Sensor.MODE_IR_PROX)