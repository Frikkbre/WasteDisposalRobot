#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import matplotlib.pyplot as plt
import numpy as np

import csv




# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

class Robot:
    def __init__(self):
        self.left_motor = Motor(Port.C)
        self.right_motor = Motor(Port.B)
        self.drive_base = DriveBase(self.left_motor, self.right_motor, 56, 114)
        #self.color_sensor = ColorSensor(Port.S3)
        #self.touch_sensor = TouchSensor(Port.S1)
        self.gyro_sensor = GyroSensor(Port.S1)
        self.ultrasonic_sensor = UltrasonicSensor(Port.S2)
        self.ev3 = EV3Brick()

class Map:
    gridSize = 12
    heatMap = np.zeros((gridSize, gridSize))
    
    
    
    
with open('writingTest.csv', 'w') as f:
    writer = csv.writer(f)
    ev3 = Robot()
    def runRobot():
        list = [1,2,3,4,5]
        while ev3.right_motor.angle() < 2000:
            ev3.drive(200,200)
            list.append(ev3.right_motor.angle())
            print(list)
        
        writer.writerow(list)
            
    runRobot()
        
        
