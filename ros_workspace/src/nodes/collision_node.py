#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from jetbot_navigation.msg import Obstacle
from cv_bridge import CvBridge
import cv2

bridge = CvBridge()
pub = rospy.Publisher("/collision_status", Obstacle, queue_size=10)

def callback(msg):

    frame = bridge.imgmsg_to_cv2(msg, "bgr8")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    center = gray[:, 200:440]
    mean_intensity = center.mean()

    obstacle = Obstacle()

    if mean_intensity < 50:
        obstacle.detected = True
        obstacle.distance = 0.5
    else:
        obstacle.detected = False
        obstacle.distance = 2.0

    pub.publish(obstacle)

rospy.init_node("collision_node")
rospy.Subscriber("/camera/image_raw", Image, callback)
rospy.spin()