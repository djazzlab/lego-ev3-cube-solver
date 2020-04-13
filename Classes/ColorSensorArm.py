from ev3dev2.motor import MediumMotor
from ev3dev2.motor import SpeedDPS
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sound import Sound

class ColorSensorArm:
    Motor = None
    Sensor = None

    def __init__(self, MotorPort, SensorPort):
        self.Motor = MediumMotor(address = MotorPort)
        self.Sensor = ColorSensor(address = SensorPort)

        # Initialize color sensor arm. First rotate the motor until it stalls.
        self.PutAway()

    def Calibrate(self):
        self.TakeOut()
        self.Sensor.calibrate_white()
        self.PutAway()

    def GetColor(self):
        self.TakeOut()
        RetrievedColor = self.Sensor.rgb
        self.PutAway()

        return RetrievedColor

    def PutAway(self):
        self.Motor.on(speed = SpeedDPS(500), block = True)
        self.Motor.off()
        self.Motor.reset()

    def TakeOut(self):
        self.Motor.on_for_rotations(speed = SpeedDPS(500), rotations = -2.2, block = True)
        self.Motor.off()