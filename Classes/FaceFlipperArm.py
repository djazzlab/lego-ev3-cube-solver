from ev3dev2.motor import LargeMotor
from ev3dev2.motor import SpeedDPS
from ev3dev2.sound import Sound

class FaceFlipperArm:
    Motor = None

    def __init__(self, MotorPort):
        self.Motor = LargeMotor(address = MotorPort)

        # Initialize face switcher arm
        self.PutAway()

    def FlipFace(self):
        # Move the arm down on the cube and start face flipping
        self.Motor.on_to_position(speed = SpeedDPS(100), position = 240, block = True)
        self.Motor.off(brake = True)

        # Move to the initial position
        self.PutAway()

    def PutAway(self):
        self.Motor.on(speed = SpeedDPS(-100), block = True)
        self.Motor.off(brake = True)
        self.Motor.reset()