#!/bin/bash

echo "Starting Visual Odometry..."

cd ../visual_odometry

python3 vo_main.py &

VO_PID=$!
echo $VO_PID > ../launch/vo.pid

echo "Visual Odometry started with PID $VO_PID"