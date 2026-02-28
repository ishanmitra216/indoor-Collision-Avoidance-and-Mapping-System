#!/bin/bash

echo "Starting Mapping Module..."

cd ../mapping

python3 grid_mapper.py &

MAP_PID=$!
echo $MAP_PID > ../launch/mapping.pid

echo "Mapping started with PID $MAP_PID"