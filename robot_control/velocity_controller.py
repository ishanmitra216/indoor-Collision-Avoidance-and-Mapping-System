from motor_controller import MotorController
from robot_state import RobotState

class VelocityController:

    def __init__(self):
        self.motor = MotorController()
        self.state = RobotState()

    def move_forward(self, speed=0.3):

        self.motor.set_velocity(speed, 0.0)
        self.state.update_velocity(speed, 0.0)
        self.state.update_status("MOVING_FORWARD")

    def move_backward(self, speed=0.3):

        self.motor.set_velocity(-speed, 0.0)
        self.state.update_velocity(-speed, 0.0)
        self.state.update_status("MOVING_BACKWARD")

    def rotate_left(self, angular_speed=1.0):

        self.motor.set_velocity(0.0, angular_speed)
        self.state.update_velocity(0.0, angular_speed)
        self.state.update_status("ROTATING_LEFT")

    def rotate_right(self, angular_speed=1.0):

        self.motor.set_velocity(0.0, -angular_speed)
        self.state.update_velocity(0.0, -angular_speed)
        self.state.update_status("ROTATING_RIGHT")

    def stop(self):

        self.motor.stop()
        self.state.update_velocity(0.0, 0.0)
        self.state.update_status("STOPPED")

    def get_robot_state(self):
        return self.state.get_state()