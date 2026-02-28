#!/bin/bash

echo "Installing Python dependencies..."
pip3 install opencv-python numpy fastapi uvicorn pyyaml sqlite3

echo "Installing ROS dependencies..."
sudo apt update
sudo apt install ros-melodic-cv-bridge ros-melodic-tf

echo "Installation Complete!"