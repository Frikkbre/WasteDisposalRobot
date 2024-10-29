#test file for claw feature.

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait
import time as t

# Creating objects
ev3 = EV3Brick()


class wasteDisposalRobot:
    def __init__(self):
        
        self.claw = Motor(Port.A, Direction.CLOCKWISE)

        self.gyroSensor = GyroSensor(Port.S1)
        


    def grip(self):
        self.claw.run_angle(90,90)

    def release(self):
       self.claw.run_angle(90,-90)


def testRobot():
    robot = wasteDisposalRobot()
    
    robot.grip()
    
    t.sleep(5)
    
    robot.release()


# Run the test
testRobot()