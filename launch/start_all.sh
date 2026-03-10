#!/bin/bash

# Unix-only launcher – see `python launch/manage.py` for a cross-platform
# (Windows/Linux/macOS) alternative that uses the same Python interpreter.

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