#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

rospy.init_node("camera_node")
pub = rospy.Publisher("/camera/image_raw", Image, queue_size=10)

bridge = CvBridge()
cap = cv2.VideoCapture(0)

rate = rospy.Rate(30)

while not rospy.is_shutdown():
    ret, frame = cap.read()
    if ret:
        msg = bridge.cv2_to_imgmsg(frame, "bgr8")
        pub.publish(msg)
    rate.sleep()