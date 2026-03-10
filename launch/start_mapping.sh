#!/bin/bash

# Unix-only helper; the Python launcher (`python launch/manage.py start`)
# will also start this module on any platform.

echo "Starting Mapping Module..."

cd ../mapping

python3 grid_mapper.py &

MAP_PID=$!
echo $MAP_PID > ../launch/mapping.pid

echo "Mapping started with PID $MAP_PID"