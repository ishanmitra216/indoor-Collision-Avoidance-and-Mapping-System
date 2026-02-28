cmake_minimum_required(VERSION 3.0.2)
project(jetbot_navigation)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  sensor_msgs
  geometry_msgs
  nav_msgs
  message_generation
)

add_message_files(
  FILES
  Pose.msg
  Map.msg
  Obstacle.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS message_runtime
)

catkin_install_python(PROGRAMS
  nodes/camera_node.py
  nodes/vo_node.py
  nodes/mapping_node.py
  nodes/collision_node.py
  nodes/motor_node.py
  nodes/database_node.py
  nodes/tf_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)