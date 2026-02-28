class RobotState:

    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        self.linear_velocity = 0.0
        self.angular_velocity = 0.0

        self.status = "IDLE"

    def update_pose(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta

    def update_velocity(self, linear, angular):
        self.linear_velocity = linear
        self.angular_velocity = angular

    def update_status(self, status):
        self.status = status

    def get_state(self):
        return {
            "x": self.x,
            "y": self.y,
            "theta": self.theta,
            "linear_velocity": self.linear_velocity,
            "angular_velocity": self.angular_velocity,
            "status": self.status
        }