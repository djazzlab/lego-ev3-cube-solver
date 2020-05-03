# EV3
from ev3dev2.sensor.lego import InfraredSensor

# Local resources
from Classes.Robot.Ev3Sensor import Ev3Sensor

class RedEyes(Ev3Sensor):
    #
    # Init
    # Initialize the sensor
    def __init__(self, SensorPort):
        super().__init__(Sensor = InfraredSensor(address = SensorPort))

    #
    # InitSensor
    # Initialize the sensor
    def InitSensor(self):
        self.SetModeIRProx()
