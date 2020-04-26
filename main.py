#!/usr/bin/env python3

# EV3 Motors
from ev3dev2.motor import OUTPUT_A as OutPortA
from ev3dev2.motor import OUTPUT_B as OutPortB
from ev3dev2.motor import OUTPUT_C as OutPortC

# EV3 Sensors
from ev3dev2.sensor import INPUT_1 as InPort1
from ev3dev2.sensor import INPUT_2 as InPort2

# Local resources
from Classes.BrickButton import BrickButton
from Classes.BrickVoice import BrickVoice
from Classes.ColorSensorArm import ColorSensorArm
from Classes.RedEyes import RedEyes
from Classes.ShufflerArm import ShufflerArm
from Classes.TurnTable import TurnTable

# Python
from time import sleep as Sleep

#
# INITIALIZATION
#
# Speaker
Speaker = BrickVoice()
Speaker.Speak(Message = 'Welcome to the E V 3 Cube Solver machine!')

Speaker.Speak(Message = 'Initialization of the robot...')

# Configure the EV3 cube face flipper arm on output port A
Ev3ShufflerArm = ShufflerArm(MotorPort = OutPortA)

# Configure the EV3 rotation platform on output port B
Ev3TurnTable = TurnTable(MotorPort = OutPortB)

# Configure the EC3 infrared sensor on input port 1
Ev3RedEyes = RedEyes(SensorPort = InPort1)

# Configure the EV3 color sensor arm on input port 2
Ev3ColorSensorArm = ColorSensorArm(MotorPort = OutPortC, SensorPort = InPort2)

# Align the platform using the brick buttons
Speaker.Speak(Message = 'Please align the turn table using the left and right brick buttons, press enter when you are good!')
Ev3Button = BrickButton()
# Rotation platform calibration
# +/- 3 degrees because the ratio between the wheels is 3 (12 and 36 pins)
# So to rotate the big wheel for 1 degree, the small one (and therefor the motor) has to rotate for 3 degrees
Ev3Button.ButtonLeftCallbackFunc = Ev3TurnTable.TurnForDegrees
Ev3Button.ButtonLeftCallbackArgs['Degrees'] = -3
Ev3Button.ButtonRightCallbackFunc = Ev3TurnTable.TurnForDegrees
Ev3Button.ButtonRightCallbackArgs['Degrees'] = 3

while True:
    if Ev3Button.Button.enter:
        break

    Ev3Button.Button.process()
    Sleep(.01)

# Initialize the cube position
Ev3ShufflerArm.PutArmDown()
Sleep(.5)
Ev3ShufflerArm.PutAway()

# Reset the rotation platform
Ev3TurnTable.InitPosition()
Ev3RedEyes.SaveProximity()

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

#
# START
#
for X in range(4):
    Ev3ColorSensorArm.TakeOut(Degrees = -549)
    Speaker.Speak(Message = Ev3ColorSensorArm.GetColor())
    Sleep(1)
    Ev3TurnTable.HalfQuarterRotate()

    Ev3ColorSensorArm.TakeOut(Degrees = 60)
    Speaker.Speak(Message = Ev3ColorSensorArm.GetColor())
    Sleep(1)
    Ev3TurnTable.HalfQuarterRotate()

    Ev3ColorSensorArm.PutAway()
    Ev3ShufflerArm.PutArmDown()
    Sleep(1)
    Ev3ShufflerArm.PutAway()

    Ev3ColorSensorArm.TakeOut(Degrees = -549)
    Speaker.Speak(Message = Ev3ColorSensorArm.GetColor())
    Sleep(1)
    Ev3TurnTable.HalfQuarterRotate()
    
    Ev3ColorSensorArm.TakeOut(Degrees = 60)
    Speaker.Speak(Message = Ev3ColorSensorArm.GetColor())
    Sleep(1)
    Ev3TurnTable.HalfQuarterRotate()
    
    Ev3ColorSensorArm.PutAway()
    Ev3ShufflerArm.PutArmDown()
    Sleep(1)
    Ev3ShufflerArm.PutAway()

    Ev3ColorSensorArm.TakeOut(Degrees = -549)
    Speaker.Speak(Message = Ev3ColorSensorArm.GetColor())
    Sleep(1)
    Ev3TurnTable.HalfQuarterRotate()
    
    Ev3ColorSensorArm.TakeOut(Degrees = 60)
    Speaker.Speak(Message = Ev3ColorSensorArm.GetColor())
    Sleep(1)
    Ev3TurnTable.HalfQuarterRotate()
    
    Ev3ColorSensorArm.PutAway()
    Ev3ShufflerArm.PutArmDown()
    Sleep(1)
    Ev3ShufflerArm.PutAway()

    Ev3ColorSensorArm.TakeOut(Degrees = -549)
    Speaker.Speak(Message = Ev3ColorSensorArm.GetColor())
    Sleep(1)
    Ev3TurnTable.HalfQuarterRotate()
    
    Ev3ColorSensorArm.TakeOut(Degrees = 60)
    Speaker.Speak(Message = Ev3ColorSensorArm.GetColor())
    Sleep(1)
    Ev3TurnTable.HalfQuarterRotate()
    
    Ev3ColorSensorArm.PutAway()
    Ev3ShufflerArm.FlipFace()
