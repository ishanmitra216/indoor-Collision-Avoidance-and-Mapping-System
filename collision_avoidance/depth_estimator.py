import cv2
import numpy as np

class DepthEstimator:

    def __init__(self):
        self.prev_gray = None

    def estimate(self, frame):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if self.prev_gray is None:
            self.prev_gray = gray
            return None

        flow = cv2.calcOpticalFlowFarneback(
            self.prev_gray,
            gray,
            None,
            0.5,
            3,
            15,
            3,
            5,
            1.2,
            0
        )

        magnitude, _ = cv2.cartToPolar(flow[...,0], flow[...,1])

        avg_motion = np.mean(magnitude)

        self.prev_gray = gray

        # Simple inverse relationship
        if avg_motion > 0:
            distance = 1.0 / avg_motion
        else:
            distance = 10.0

        return distance