#!/bin/bash

echo "====================================="
echo " Starting JetBot Indoor Navigation "
echo "====================================="

bash start_vo.sh
sleep 2

bash start_mapping.sh
sleep 2

bash start_api.sh
sleep 2

bash start_dashboard.sh

echo "====================================="
echo " All Modules Started Successfully "
echo "====================================="