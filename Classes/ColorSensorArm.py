# EV3
from ev3dev2.button import Button
from ev3dev2.motor import MediumMotor, SpeedDPS
from ev3dev2.sensor.lego import ColorSensor

# Python
from time import sleep as Sleep

class ColorSensorArm:
    Button = None
    ColorIntensities = {
        'Blue': 0,
        'Green': 0,
        'Orange': 0,
        'Red': 0,
        'White': 0,
        'Yellow': 0
    }
    Motor = None
    Sensor = None
    TotalDegrees = 0

    #
    # Init
    # Initialize color sensor arm. First rotate the motor until it stalls.
    def __init__(self, MotorPort, SensorPort):
        self.Button = Button()
        self.Motor = MediumMotor(address = MotorPort)
        self.Sensor = ColorSensor(address = SensorPort)
        self.Sensor.mode = 'COL-REFLECT'
        self.PutAway()

    #
    # CalibrateSensor
    # Calibrate the sensor by asking the operator the color
    # in front of the sensor using the brick buttons 
    def CalibrateSensor(self):
        # Wait for a button to be pressed
        # Timeout is 5 sec        
        ElapsedTime = 0
        while len(self.Button.buttons_pressed) == 0:
            if ElapsedTime > 5:
                break
            ElapsedTime += .1
            Sleep(.1)
        
        if self.Button.up:
            for X in range(3):
                self.ColorIntensities['Blue'] += self.Sensor.reflected_light_intensity
                Sleep(.5)
            self.ColorIntensities['Blue'] = self.ColorIntensities['Blue'] // 3
            return 'Blue'

        elif self.Button.right:
            for X in range(3):
                self.ColorIntensities['Green'] += self.Sensor.reflected_light_intensity
                Sleep(.5)
            self.ColorIntensities['Green'] = self.ColorIntensities['Green'] // 3
            return 'Green'

        elif self.Button.down:
            for X in range(3):
                self.ColorIntensities['Orange'] += self.Sensor.reflected_light_intensity
                Sleep(.5)
            self.ColorIntensities['Orange'] = self.ColorIntensities['Orange'] // 3
            return 'Orange'

        elif self.Button.left:
            for X in range(3):
                self.ColorIntensities['Red'] += self.Sensor.reflected_light_intensity
                Sleep(.5)
            self.ColorIntensities['Red'] = self.ColorIntensities['Red'] // 3
            return 'Red'

        elif self.Button.enter:
            for X in range(3):
                self.ColorIntensities['Yellow'] += self.Sensor.reflected_light_intensity
                Sleep(.5)
            self.ColorIntensities['Yellow'] = self.ColorIntensities['Yellow'] // 3
            return 'Yellow'
        
        else:
            for X in range(3):
                self.ColorIntensities['White'] += self.Sensor.reflected_light_intensity
                Sleep(.5)
            self.ColorIntensities['White'] = self.ColorIntensities['White'] // 3
            return 'White'

    #
    # GetColor
    # Return the color in front of the sensor
    def GetColor(self):
        RetrievedColors = []
        
        # Grab colors from the sensor
        Intensity = 0
        for X in range(3):
            Intensity += self.Sensor.reflected_light_intensity
            Sleep(.5)
        Intensity = Intensity // 3
        print(Intensity)
        Color = None
        IntensityDistance = 0
        for ColorName in self.ColorIntensities.keys():
            TmpDistance = abs(self.ColorIntensities[ColorName] - Intensity)

            if Color is None or TmpDistance < IntensityDistance:
                IntensityDistance = TmpDistance
                Color = ColorName

        return Color

    #
    # MotorOff
    # Shutdown the motor 
    def MotorOff(self, Reset = False):
        self.Motor.off(brake = True)
        if Reset:
            self.Motor.reset()
            self.TotalDegrees = 0

    #
    # PutAway
    # Put the arm away
    def PutAway(self):
        self.Motor.on(speed = SpeedDPS(500), block = True)
        self.MotorOff(Reset = True)

    #
    # TakeOut
    # Take the arm out
    def TakeOut(self, Degrees):
        self.TotalDegrees += Degrees
        print('Current degrees: {}'.format(self.TotalDegrees))
        self.Motor.on_for_degrees(speed = SpeedDPS(150), degrees = Degrees, block = True)
        
        if self.TotalDegrees >= 1080:
            self.MotorOff(Reset = True)
        else:
            self.MotorOff()
