#!/bin/bash

echo "Setting up ROS Workspace..."

cd ~/ros_workspace
catkin_make

echo "Sourcing workspace..."
echo "source ~/ros_workspace/devel/setup.bash" >> ~/.bashrc

source devel/setup.bash

echo "ROS Setup Complete!"