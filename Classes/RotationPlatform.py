from ev3dev2.motor import LargeMotor
from ev3dev2.motor import SpeedDPS
from ev3dev2.sound import Sound

class RotationPlatform:
    Motor = None

    def __init__(self, MotorPort):
        self.Motor = LargeMotor(address = MotorPort)

        # Initialize rotation platform
        self.Motor.off(brake = True)
        self.Motor.reset()

    def Rotate(self, Degrees):
        self.Motor.on_for_degrees(speed = SpeedDPS(150), degrees = Degrees, block = True)
        self.Motor.off(brake = True)

    def RotateOff(self):
        self.Motor.off(brake = True)

    def RotateOn(self):
        self.Motor.on(speed = SpeedDPS(150))
        self.Motor.wait_until_not_moving()
        