class AvoidanceController:

    def __init__(self, safe_distance=0.5):
        self.safe_distance = safe_distance

    def decide(self, obstacle_detected, distance):

        if obstacle_detected:

            if distance is not None and distance < self.safe_distance:
                return "STOP"

            return "TURN_LEFT"

        return "FORWARD"