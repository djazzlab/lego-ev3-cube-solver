#!/usr/bin/env python3

from Classes.BrickVoice import BrickVoice
from Classes.ColorSensorArm import ColorSensorArm
from Classes.FaceFlipperArm import FaceFlipperArm
from Classes.RotationPlatform import RotationPlatform

# Inputs
from ev3dev2.sensor import INPUT_2 as InPort2

# Outputs
from ev3dev2.motor import OUTPUT_A as OutPortA
from ev3dev2.motor import OUTPUT_B as OutPortB
from ev3dev2.motor import OUTPUT_C as OutPortC

from time import sleep as Sleep
#
# INITIALIZATION
#
# Speaker
Speaker = BrickVoice()
Speaker.Speak(Message = 'Welcome to the E V 3 Cube Solver machine!')

Speaker.Speak(Message = 'Initialization of the robot...')

# Configure the EV3 cube face flipper arm on output port A
Ev3FaceFlipperArm = FaceFlipperArm(MotorPort = OutPortA)

# Configure the EV3 rotation platform on output port B
Ev3RotationPlatform = RotationPlatform(MotorPort = OutPortB)

# Configure the EV3 color sensor arm on output port C
Ev3ColorSensorArm = ColorSensorArm(MotorPort = OutPortC, SensorPort = InPort2)

# Color sensor calibration
Speaker.Speak(Message = 'Please, calibrate the color sensor. Press up for blue, right for green, down for orange, left for red, enter for yellow, nothing for white.')
for X in range(4):
    Ev3ColorSensorArm.TakeOut(Position = -750)
    Speaker.Speak(Message = 'What is the top face color of the cube?')
    Speaker.Speak(Message = '{} face calibrated.'.format(Ev3ColorSensorArm.Calibrate()))
    Ev3ColorSensorArm.PutAway()
    Ev3FaceFlipperArm.FlipFace()

# 1/4 Rotation of the platform + 1 flip
Ev3RotationPlatform.Rotate(Degrees = 268)
Ev3FaceFlipperArm.FlipFace()

# Continue calibration
Ev3ColorSensorArm.TakeOut(Position = -750)
Speaker.Speak(Message = 'What is the top face color of the cube?')
Speaker.Speak(Message = '{} face calibrated.'.format(Ev3ColorSensorArm.Calibrate()))
Ev3ColorSensorArm.PutAway()

Ev3FaceFlipperArm.FlipFace()
Ev3FaceFlipperArm.FlipFace()

Ev3ColorSensorArm.TakeOut(Position = -750)
Speaker.Speak(Message = 'What is the top face color of the cube?')
Speaker.Speak(Message = '{} face calibrated.'.format(Ev3ColorSensorArm.Calibrate()))
Ev3ColorSensorArm.PutAway()

Speaker.Speak(Message = 'Thank you!')

#
# START
#
for X in range(4):
    Ev3ColorSensorArm.TakeOut(Position = -640)
    Speaker.Speak(Message = Ev3ColorSensorArm.GetColor())
    Sleep(1)
    Ev3RotationPlatform.Rotate(Degrees = 110)
    Ev3ColorSensorArm.TakeOut(Position = -580)
    Speaker.Speak(Message = Ev3ColorSensorArm.GetColor())
    Sleep(1)
    Ev3RotationPlatform.Rotate(Degrees = 140)
    Ev3ColorSensorArm.TakeOut(Position = -660)
    Speaker.Speak(Message = Ev3ColorSensorArm.GetColor())
    Sleep(1)
    Ev3RotationPlatform.Rotate(Degrees = 110)
    Ev3ColorSensorArm.TakeOut(Position = -580)
    Speaker.Speak(Message = Ev3ColorSensorArm.GetColor())
    Sleep(1)
    Ev3RotationPlatform.Rotate(Degrees = 140)
    Ev3ColorSensorArm.TakeOut(Position = -660)
    Speaker.Speak(Message = Ev3ColorSensorArm.GetColor())
    Sleep(1)
    Ev3RotationPlatform.Rotate(Degrees = 110)
    Ev3ColorSensorArm.TakeOut(Position = -580)
    Speaker.Speak(Message = Ev3ColorSensorArm.GetColor())
    Sleep(1)
    Ev3RotationPlatform.Rotate(Degrees = 140)
    Ev3ColorSensorArm.TakeOut(Position = -660)
    Speaker.Speak(Message = Ev3ColorSensorArm.GetColor())
    Sleep(1)
    Ev3RotationPlatform.Rotate(Degrees = 110)
    Ev3ColorSensorArm.TakeOut(Position = -580)
    Speaker.Speak(Message = Ev3ColorSensorArm.GetColor())
    Ev3FaceFlipperArm.FlipFace()
