#!/bin/bash

echo "Starting Dashboard..."

cd ../dashboard

python3 -m http.server 8080 &

DASH_PID=$!
echo $DASH_PID > ../launch/dashboard.pid

echo "Dashboard running at http://localhost:8080"