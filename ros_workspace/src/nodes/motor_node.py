#!/usr/bin/env python3
import rospy
from jetbot_navigation.msg import Obstacle
from jetbot import Robot

robot = Robot()

def callback(msg):

    if msg.detected:
        robot.stop()
    else:
        robot.forward(0.3)

rospy.init_node("motor_node")
rospy.Subscriber("/collision_status", Obstacle, callback)
rospy.spin()