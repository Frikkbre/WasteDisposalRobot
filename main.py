#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait
import time as t

# Creating objects
ev3 = EV3Brick()


class RallyRobot():
    def __init__(self):
        
        # Initializing motors.
        self.leftBelt = Motor(Port.C, Direction.COUNTERCLOCKWISE)
        self.rightBelt = Motor(Port.B, Direction.COUNTERCLOCKWISE)
        
        self.claw = Motor(Port.A, Direction.CLOCKWISE)

        self.colorSensor = ColorSensor(Port.S1)
        self.distanceSensor = UltrasonicSensor(Port.S2)

        # Initializing the drivebase.
        self.robot = DriveBase(self.leftBelt, self.rightBelt)

        # Defining proportional gain, drive speed and turn speed
        #self.PROPORTIONAL_GAIN = 9
        #self.DRIVE_SPEED = 150 
        #self.TURN_SPEED = 100
        

def grip():
    #Grip box
    pass

def release():
    #release box
    pass

def catchBox(colorSensor, distanceSensor):
    grip()

