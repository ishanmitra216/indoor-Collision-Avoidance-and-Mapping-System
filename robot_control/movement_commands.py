import time
from velocity_controller import VelocityController

class MovementCommands:

    def __init__(self):
        self.controller = VelocityController()

    def go_forward_distance(self, speed, duration):

        self.controller.move_forward(speed)
        time.sleep(duration)
        self.controller.stop()

    def turn_left_angle(self, angular_speed, duration):

        self.controller.rotate_left(angular_speed)
        time.sleep(duration)
        self.controller.stop()

    def turn_right_angle(self, angular_speed, duration):

        self.controller.rotate_right(angular_speed)
        time.sleep(duration)
        self.controller.stop()

    def emergency_stop(self):
        self.controller.stop()

    def get_state(self):
        return self.controller.get_robot_state()