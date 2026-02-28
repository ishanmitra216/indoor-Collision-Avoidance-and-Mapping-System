#!/bin/bash

echo "Stopping all services..."

if [ -f vo.pid ]; then
    kill $(cat vo.pid)
    rm vo.pid
    echo "VO stopped"
fi

if [ -f mapping.pid ]; then
    kill $(cat mapping.pid)
    rm mapping.pid
    echo "Mapping stopped"
fi

if [ -f api.pid ]; then
    kill $(cat api.pid)
    rm api.pid
    echo "API stopped"
fi

if [ -f dashboard.pid ]; then
    kill $(cat dashboard.pid)
    rm dashboard.pid
    echo "Dashboard stopped"
fi

echo "All services stopped successfully!"