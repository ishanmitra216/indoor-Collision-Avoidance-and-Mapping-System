#!/bin/bash

echo "Starting API Server..."

cd ../api_server

uvicorn main:app --host 0.0.0.0 --port 8000 --reload &

API_PID=$!
echo $API_PID > ../launch/api.pid

echo "API started with PID $API_PID"