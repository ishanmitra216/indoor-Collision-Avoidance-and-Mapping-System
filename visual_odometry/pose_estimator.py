import numpy as np
import cv2

class PoseEstimator:

    def __init__(self, camera_model):
        self.camera = camera_model

    def estimate(self, kp1, kp2, matches):

        pts1 = np.float32([kp1[m.queryIdx].pt for m in matches])
        pts2 = np.float32([kp2[m.trainIdx].pt for m in matches])

        E, mask = cv2.findEssentialMat(
            pts1,
            pts2,
            focal=self.camera.focal,
            pp=self.camera.principal_point,
            method=cv2.RANSAC,
            prob=0.999,
            threshold=1.0
        )

        _, R, t, mask = cv2.recoverPose(
            E,
            pts1,
            pts2,
            focal=self.camera.focal,
            pp=self.camera.principal_point
        )

        return R, t