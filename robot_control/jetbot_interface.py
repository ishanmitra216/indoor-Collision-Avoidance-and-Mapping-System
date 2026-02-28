from jetbot import Robot

class JetBotInterface:

    def __init__(self):
        self.robot = Robot()

    def set_motors(self, left_speed, right_speed):
        self.robot.left_motor.value = left_speed
        self.robot.right_motor.value = right_speed

    def forward(self, speed=0.3):
        self.robot.forward(speed)

    def backward(self, speed=0.3):
        self.robot.backward(speed)

    def left(self, speed=0.3):
        self.robot.left(speed)

    def right(self, speed=0.3):
        self.robot.right(speed)

    def stop(self):
        self.robot.stop()