from jetbot import Robot
import time

class MotionPlanner:

    def __init__(self):
        self.robot = Robot()

    def execute(self, command):

        if command == "FORWARD":
            self.robot.forward(0.3)

        elif command == "STOP":
            self.robot.stop()

        elif command == "TURN_LEFT":
            self.robot.left(0.3)
            time.sleep(0.4)
            self.robot.stop()

        elif command == "TURN_RIGHT":
            self.robot.right(0.3)
            time.sleep(0.4)
            self.robot.stop()