import numpy as np
import matplotlib.pyplot as plt
import random
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
        leftMotor.run_angle(200, 360, wait=False)
        rightMotor.runAngle(200, 360)
        wait(1000)
        distance = ultrasonicSensor.distance()
        angle = gyroSensor.angle()
        if distance < 300:
            leftMotor.run_angle(200, 180, wait=False)
            rightMotor.runAngle(200, -180)
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
