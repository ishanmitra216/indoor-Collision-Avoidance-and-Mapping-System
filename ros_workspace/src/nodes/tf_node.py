#!/usr/bin/env python3
import rospy
import tf
from jetbot_navigation.msg import Pose

br = tf.TransformBroadcaster()

def callback(msg):

    br.sendTransform(
        (msg.x, msg.y, 0),
        tf.transformations.quaternion_from_euler(0,0,msg.theta),
        rospy.Time.now(),
        "base_link",
        "map"
    )

rospy.init_node("tf_node")
rospy.Subscriber("/robot/pose", Pose, callback)
rospy.spin()