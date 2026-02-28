import cv2

class ORBDetector:

    def __init__(self, nfeatures=2000):
        self.orb = cv2.ORB_create(nfeatures)

    def detect(self, frame):
        keypoints, descriptors = self.orb.detectAndCompute(frame, None)
        return keypoints, descriptors