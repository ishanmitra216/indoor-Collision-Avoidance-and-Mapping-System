class RobotService:

    def __init__(self):
        self.robot_state = {
            "x": 0.0,
            "y": 0.0,
            "theta": 0.0,
            "status": "IDLE"
        }

        self.collision_status = {
            "detected": False,
            "distance": 2.0
        }

    def update_state(self, x, y, theta, status):
        self.robot_state = {
            "x": x,
            "y": y,
            "theta": theta,
            "status": status
        }

    def update_collision(self, detected, distance):
        self.collision_status = {
            "detected": detected,
            "distance": distance
        }

    def get_state(self):
        return self.robot_state

    def get_collision_status(self):
        return self.collision_status