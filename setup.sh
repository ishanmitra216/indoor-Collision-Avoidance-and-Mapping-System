#!/bin/bash

echo "Installing Python packages..."
pip3 install -r requirements.txt

echo "Setting up ROS workspace..."
cd ros_workspace
catkin_make
source devel/setup.bash

echo "Initializing database..."
cd ../database/migrations
python3 init_db.py

echo "Setup completed successfully!"