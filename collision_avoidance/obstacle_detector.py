import cv2
import numpy as np

class ObstacleDetector:

    def __init__(self, intensity_threshold=50, edge_threshold=1500):
        self.intensity_threshold = intensity_threshold
        self.edge_threshold = edge_threshold

    def detect(self, frame):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Focus on center region
        h, w = gray.shape
        center_region = gray[:, w//3:2*w//3]

        # Brightness-based detection
        mean_intensity = np.mean(center_region)

        # Edge density detection
        edges = cv2.Canny(center_region, 50, 150)
        edge_count = np.sum(edges > 0)

        obstacle_detected = False

        if mean_intensity < self.intensity_threshold:
            obstacle_detected = True

        if edge_count > self.edge_threshold:
            obstacle_detected = True

        return obstacle_detected, mean_intensity, edge_count