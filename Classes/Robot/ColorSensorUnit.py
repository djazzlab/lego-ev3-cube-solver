# EV3
from ev3dev2.sensor.lego import ColorSensor

# Local resources
from Classes.Robot.Ev3Sensor import Ev3Sensor

class ColorSensorUnit(Ev3Sensor):
    #
    # Init
    # Initialize the sensor
    def __init__(self, SensorPort):
        super().__init__(Sensor = ColorSensor(address = SensorPort))
        
    #
    # InitSensor
    # Initialize the sensor
    def InitSensor(self):
        self.SetModeRGBRAW()
