from jetbot import Robot
import time

robot = Robot()

print("Forward")
robot.forward(0.3)
time.sleep(2)

print("Left")
robot.left(0.3)
time.sleep(1)

print("Stop")
robot.stop()