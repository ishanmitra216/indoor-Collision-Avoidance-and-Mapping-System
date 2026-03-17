#!/usr/bin/env python3
"""Long-running mapping service entrypoint.

This process keeps an in-memory occupancy grid alive and periodically persists
it so other modules can consume a stable map artifact even when no upstream
pose/obstacle stream is connected.
"""

import os
import signal
import time

from grid_mapper import GridMapper

RUNNING = True


def _handle_shutdown(signum, frame):
    del signum, frame
    global RUNNING
    RUNNING = False


def _save_snapshot(mapper):
    os.makedirs("saved_maps", exist_ok=True)
    mapper.save_map("saved_maps/map_live.npy")


def main():
    signal.signal(signal.SIGTERM, _handle_shutdown)
    signal.signal(signal.SIGINT, _handle_shutdown)

    mapper = GridMapper()
    mapper.update_robot_pose(0.0, 0.0, 0.0)
    _save_snapshot(mapper)

    print("Mapping service started. Writing snapshot to mapping/saved_maps/map_live.npy")

    while RUNNING:
        _save_snapshot(mapper)
        time.sleep(1)

    _save_snapshot(mapper)
    print("Mapping service stopped.")


if __name__ == "__main__":
    main()
