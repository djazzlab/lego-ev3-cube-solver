from ev3dev2.motor import LargeMotor
from ev3dev2.motor import SpeedDPS
from ev3dev2.sound import Sound

class RotationPlatform:
    Motor = None

    def __init__(self, MotorPort):
        self.Motor = LargeMotor(address = MotorPort)

        # Initialize rotation platform
        self.Motor.off()
        self.Motor.reset()

    def Rotate(self):
        self.Motor.on_for_degrees(speed = SpeedDPS(150), degrees = 268, block = True)
        self.Motor.off()