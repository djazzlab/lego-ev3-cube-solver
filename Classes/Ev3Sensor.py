class Ev3Sensor:
    __Sensor = None

    #
    # Init
    # Initialize the sensor
    def __init__(self, Sensor):
        self.__Sensor = Sensor

    #################
    # Color Sensors #
    #################
    #
    # SetModeRGBRAW
    # Register the mode IR-PROX for the sensor
    def SetModeRGBRAW(self):
        self.__Sensor.mode = self.__Sensor.MODE_RGB_RAW

    #
    # GetRGBColor
    # Return a tuple of the RGB color code detected by the sensor
    def GetRGBColor(self):
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
        self.__Sensor.mode = self.__Sensor.MODE_IR_PROX