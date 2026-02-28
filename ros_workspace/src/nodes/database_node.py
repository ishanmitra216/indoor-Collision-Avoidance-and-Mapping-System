#!/usr/bin/env python3
import rospy
import sqlite3
from jetbot_navigation.msg import Pose

conn = sqlite3.connect("/home/jetson/robot.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pose(
id INTEGER PRIMARY KEY AUTOINCREMENT,
x REAL,
y REAL,
theta REAL
)
""")

def callback(msg):

    cursor.execute("INSERT INTO pose(x,y,theta) VALUES(?,?,?)",
                   (msg.x, msg.y, msg.theta))
    conn.commit()

rospy.init_node("database_node")
rospy.Subscriber("/robot/pose", Pose, callback)
rospy.spin()