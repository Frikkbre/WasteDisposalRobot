import numpy as np
import matplotlib.pyplot as plt
import random
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

leftBelt = Motor(Port.C, Direction.CLOCKWISE)
rightBelt = Motor(Port.B, Direction.CLOCKWISE)

distanceSensor = UltrasonicSensor(Port.S2)
gyroSensor = GyroSensor(Port.S1)

# Generate a 12x12 grid with random values to represent heatmap data
gridSize = 12
heatmap = np.zeros((gridSize, gridSize))
def updateHeatmap(x, y):
    heatmap[x, y] += 1
# Simulating robot movement.
def moveRobot(steps):
    x, y = gridSize // 2, gridSize // 2 # Will start the robot in the middle of grid.
    for _ in range(steps):
        updateHeatmap(x, y)
        leftBelt.run_angle(200, 360, wait=False)
        rightBelt.runAngle(200, 360)
        wait(1000)
        distance = UltrasonicSensor.distance()
        angle = gyroSensor.angle()
        if distance < 300:
            leftBelt.run_angle(200, 180, wait=False)
            rightBelt.runAngle(200, -180)
        else:
            x += random.choice([-1, 0, 1])
            y += random.choice([-1, 0, 1])
        x = max(0, min(gridSize - 1, x)) # Limiting the grid boundaries (x)
        y = max(0, min(gridSize - 1, y)) # Limiting the grid boundaries (y)
# Simulating 1000 steps of robot movement.
moveRobot(1000)
# Plotting the heatmap
plt.imshow(heatmap, cmap="magma", interpolation="bicubic")
plt.title("Robot Heatmap")
plt.xlabel("Distance in cm")
plt.ylabel("Distance in cm")
plt.colorbar(label="Visits")
plt.show()
