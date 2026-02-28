#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from jetbot_navigation.msg import Pose

bridge = CvBridge()
pub = rospy.Publisher("/robot/pose", Pose, queue_size=10)

orb = cv2.ORB_create(2000)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

prev_kp, prev_des = None, None
pose_matrix = np.eye(4)

def callback(msg):

    global prev_kp, prev_des, pose_matrix

    frame = bridge.imgmsg_to_cv2(msg, "bgr8")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    kp, des = orb.detectAndCompute(gray, None)

    if prev_kp is None:
        prev_kp, prev_des = kp, des
        return

    matches = bf.match(prev_des, des)
    matches = sorted(matches, key=lambda x: x.distance)[:100]

    if len(matches) > 10:

        pts1 = np.float32([prev_kp[m.queryIdx].pt for m in matches])
        pts2 = np.float32([kp[m.trainIdx].pt for m in matches])

        E, _ = cv2.findEssentialMat(pts1, pts2, focal=718, pp=(320,240))
        _, R, t, _ = cv2.recoverPose(E, pts1, pts2)

        T = np.eye(4)
        T[:3,:3] = R
        T[:3,3] = t.squeeze()

        pose_matrix = pose_matrix @ np.linalg.inv(T)

        pose_msg = Pose()
        pose_msg.x = pose_matrix[0,3]
        pose_msg.y = pose_matrix[2,3]
        pose_msg.theta = 0.0

        pub.publish(pose_msg)

    prev_kp, prev_des = kp, des

rospy.init_node("vo_node")
rospy.Subscriber("/camera/image_raw", Image, callback)
rospy.spin()