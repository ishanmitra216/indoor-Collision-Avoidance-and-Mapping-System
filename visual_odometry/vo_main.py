import cv2
import numpy as np
from orb_detector import ORBDetector
from feature_matcher import FeatureMatcher
from pose_estimator import PoseEstimator
from trajectory import Trajectory
from camera_model import CameraModel
from utils.visualization import draw_trajectory

def main():

    cap = cv2.VideoCapture(0)

    camera = CameraModel()
    orb = ORBDetector()
    matcher = FeatureMatcher()
    estimator = PoseEstimator(camera)
    trajectory = Trajectory()

    prev_frame = None
    prev_kp, prev_des = None, None

    pose = np.eye(4)

    while True:

        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        kp, des = orb.detect(gray)

        if prev_frame is None:
            prev_frame = gray
            prev_kp, prev_des = kp, des
            continue

        matches = matcher.match(prev_des, des)

        if len(matches) > 10:

            R, t = estimator.estimate(prev_kp, kp, matches)

            T = np.eye(4)
            T[:3,:3] = R
            T[:3,3] = t.squeeze()

            pose = pose @ np.linalg.inv(T)

            trajectory.update(pose)

            draw_trajectory(trajectory.positions)

        prev_frame = gray
        prev_kp, prev_des = kp, des

        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()