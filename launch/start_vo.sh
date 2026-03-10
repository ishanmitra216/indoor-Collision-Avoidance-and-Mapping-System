#!/bin/bash

# Unix-only helper; the Python launcher (`python launch/manage.py start`)
# will also start this module on any platform.

echo "Starting Visual Odometry..."

cd ../visual_odometry

python3 vo_main.py &

VO_PID=$!
echo $VO_PID > ../launch/vo.pid

echo "Visual Odometry started with PID $VO_PID"