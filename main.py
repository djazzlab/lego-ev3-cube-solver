#!/usr/bin/env python3

from Classes.ColorSensorArm import ColorSensorArm
from Classes.FaceFlipperArm import FaceFlipperArm
from Classes.RotationPlatform import RotationPlatform

# Inputs
from ev3dev2.sensor import INPUT_2 as InPort2

# Outputs
from ev3dev2.motor import OUTPUT_A as OutPortA
from ev3dev2.motor import OUTPUT_B as OutPortB
from ev3dev2.motor import OUTPUT_C as OutPortC

#
# INITIALIZATION
#
# Speaker
# Speaker = Sound()
# Speaker.speak('Welcome to the E V 3 Cube Solver machine!')
# Speaker.speak('Initialization phase')

# Configure the EV3 cube face flipper arm on output port A
Ev3FaceFlipperArm = FaceFlipperArm(MotorPort = OutPortA)

# Configure the EV3 rotation platform on output port B
Ev3RotationPlatform = RotationPlatform(MotorPort = OutPortB)

# Configure the EV3 color sensor arm on output port C
Ev3ColorSensorArm = ColorSensorArm(MotorPort = OutPortC, SensorPort = InPort2)
Ev3ColorSensorArm.Calibrate()

# Faces of the cube, named with the color of the middle sticker
CubeFaces = []

#
# START
#
for X in range(4):
    CubeFaces = []
    
    for X in range(4):
        print(Ev3ColorSensorArm.GetColor())
        Ev3FaceFlipperArm.FlipFace()
    
    print('')