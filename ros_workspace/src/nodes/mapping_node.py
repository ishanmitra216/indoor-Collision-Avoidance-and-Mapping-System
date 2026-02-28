#!/usr/bin/env python3
import rospy
import numpy as np
from jetbot_navigation.msg import Pose
from nav_msgs.msg import OccupancyGrid

grid = np.zeros((200,200), dtype=np.int8)

pub = rospy.Publisher("/map", OccupancyGrid, queue_size=10)

def pose_callback(msg):

    x = int(msg.x * 10) + 100
    y = int(msg.y * 10) + 100

    if 0 <= x < 200 and 0 <= y < 200:
        grid[y,x] = 100

    map_msg = OccupancyGrid()
    map_msg.info.width = 200
    map_msg.info.height = 200
    map_msg.data = grid.flatten().tolist()

    pub.publish(map_msg)

rospy.init_node("mapping_node")
rospy.Subscriber("/robot/pose", Pose, pose_callback)
rospy.spin()