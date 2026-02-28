import cv2
from collision_avoidance.obstacle_detector import ObstacleDetector

detector = ObstacleDetector()

frame = cv2.imread("test.jpg")
result = detector.detect(frame)

print("Collision detection result:", result)