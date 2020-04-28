#
# CalibrateSensor
# Calibrate the sensor by asking the operator the color
# in front of the sensor using the brick buttons 
def CalibrateSensor(self):
    # Color sensor calibration
    Speaker.Speak(Message = 'Please, calibrate the color sensor. Press up for blue, right for green, down for orange, left for red, enter for yellow, nothing for white.')
    for X in range(4):
        Ev3ColorSensorArm.TakeOut(Degrees = -636)
        Speaker.Speak(Message = 'What is the top face color of the cube?')
        Speaker.Speak(Message = '{} face calibrated.'.format(Ev3ColorSensorArm.CalibrateSensor()))
        Ev3ColorSensorArm.PutAway()
        Ev3ShufflerArm.FlipFace()

    # 1/4 Rotation of the platform + 1 flip
    Ev3TurnTable.QuarterRotate()
    Ev3ShufflerArm.FlipFace()

    # Continue calibration
    Ev3ColorSensorArm.TakeOut(Degrees = -636)
    Speaker.Speak(Message = 'What is the top face color of the cube?')
    Speaker.Speak(Message = '{} face calibrated.'.format(Ev3ColorSensorArm.CalibrateSensor()))
    Ev3ColorSensorArm.PutAway()

    for X in range(2):
        Ev3ShufflerArm.FlipFace()

    Ev3ColorSensorArm.TakeOut(Degrees = -636)
    Speaker.Speak(Message = 'What is the top face color of the cube?')
    Speaker.Speak(Message = '{} face calibrated.'.format(Ev3ColorSensorArm.CalibrateSensor()))
    Ev3ColorSensorArm.PutAway()

    Speaker.Speak(Message = 'Thank you!')

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