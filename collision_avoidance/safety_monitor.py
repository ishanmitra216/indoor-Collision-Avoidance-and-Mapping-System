import time

class SafetyMonitor:

    def __init__(self, timeout=2.0):
        self.last_detection_time = time.time()
        self.timeout = timeout

    def update_detection(self, detected):

        if detected:
            self.last_detection_time = time.time()

    def check_emergency(self):

        if time.time() - self.last_detection_time > self.timeout:
            return True

        return False