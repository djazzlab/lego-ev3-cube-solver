# EV3
from ev3dev2.sensor.lego import InfraredSensor

class RedEyes:
    Sensor = None
    SavedProximity = 0

    #
    # Init
    # Initialize the sensor
    def __init__(self, SensorPort):
        self.Sensor = InfraredSensor(address = SensorPort)

        # Init the sensor
        self.__SetMode(Mode = 'IR-PROX')

    ###################
    # Exposed Methods #
    ###################

    #
    # GetProximity
    # Return the distance between the eyes and the cube
    def GetProximity(self):
        return self.Sensor.proximity

    #
    # SaveProximity
    # Save the current proximity
    def SaveProximity(self):
        self.SavedProximity = self.GetProximity()

    ###################
    # Private Methods #
    ###################

    #
    # SetMode
    # Register the mode of the sensor
    def __SetMode(self, Mode):
        self.Sensor.mode = Mode