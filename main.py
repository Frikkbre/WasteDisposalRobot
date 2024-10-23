#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait
import time as t

# Creating objects
ev3 = EV3Brick()


class wasteDisposalRobot:
    def __init__(self):
        
        # Initializing motors.
        self.leftBelt = Motor(Port.C, Direction.CLOCKWISE)
        self.rightBelt = Motor(Port.B, Direction.CLOCKWISE)
        
        self.claw = Motor(Port.A, Direction.COUNTERCLOCKWISE)

        #self.colorSensor = ColorSensor(Port.S1)
        self.distanceSensor = UltrasonicSensor(Port.S2)

        # Initializing the drivebase.
        self.robot = DriveBase(self.leftBelt, self.rightBelt, wheel_diameter=56, axle_track=114)  # Add wheel_diameter and axle_track for accurate movement

    def drive(self, speed_left, speed_right):
        # Drive the robot with a specific speed for the left and right wheels
        self.robot.drive(speed_left, speed_right)

    def grip(self):
        self.claw.run(2000)
        #self.claw.run_target(50, 0)  # Assuming 0 is the closed position
        

    def release(self):
        self.claw.run_target(50, 90)  # Assuming 90 is the open position
       


def testRobot():
    robot = wasteDisposalRobot()
    
    while robot.distanceSensor.distance() > 200:
        #(Straight, turn(+ = R,   - = L))
        #robot.drive(200, 0)
        robot.grip()
        #wait(10)
        #robot.release
        
    robot.drive(0,0)


# Run the test
testRobot()