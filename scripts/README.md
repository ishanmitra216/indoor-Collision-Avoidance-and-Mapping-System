# Scripts Module

This folder contains utility scripts for setup, calibration, dependency
installation, and quick hardware/system checks.

## Purpose

- Help prepare the environment for development/runtime.
- Validate hardware and system prerequisites.
- Provide quick diagnostics for camera and motors.

## File Components

### calibrate_camera.py

Camera calibration utility using checkerboard images.

What it does:
- Loads images from `calibration_images/*.jpg`.
- Detects checkerboard corners (`CHECKERBOARD = (6, 9)`).
- Builds object/image point correspondences.
- Runs `cv2.calibrateCamera(...)`.
- Prints camera matrix and distortion coefficients.

Use when:
- You need camera intrinsics for better visual odometry accuracy.

### test_camera.py

Live camera validation script.

What it does:
- Opens camera index `0`.
- Displays real-time feed in an OpenCV window.
- Exits on `Esc` key.

Use when:
- You want to quickly confirm camera availability and stream quality.

### test_motors.py

Basic JetBot motor movement test.

What it does:
- Initializes `jetbot.Robot`.
- Executes short sequence:
	- Forward
	- Left turn
	- Stop

Use when:
- You want to verify motor driver and directional control.

Note:
- Should be run on real JetBot-compatible hardware.

### system_check.py

Simple end-to-end sanity check script.

What it does:
- Runs camera test script.
- Checks SQLite database tables via shell command.
- Prints progress messages.

Use when:
- You need a quick pre-run confidence check before launching the full stack.

### install_dependencies.sh

Environment bootstrap script for Linux-based setup.

What it does:
- Installs Python packages with `pip3`.
- Installs ROS-related apt packages.

Note:
- Script currently includes `sqlite3` in `pip3 install`, but SQLite is usually
	provided as a system package / Python standard library integration rather
	than a pip package.

### setup_ros.sh

ROS workspace setup helper.

What it does:
- Builds ROS workspace with `catkin_make`.
- Appends workspace source command to shell startup (`~/.bashrc`).
- Sources generated setup file.

Use when:
- Initializing ROS workspace environment on Linux.

## Recommended Usage Order

1. Run dependency install script (`install_dependencies.sh`) on Linux.
2. Run ROS setup (`setup_ros.sh`) if ROS features are used.
3. Run camera calibration (`calibrate_camera.py`) if intrinsics are needed.
4. Validate hardware with `test_camera.py` and `test_motors.py`.
5. Run `system_check.py` before full launch.

## Notes

- Shell scripts are Unix-oriented; use equivalent Windows commands when needed.
- Hardware tests should be performed in a safe, open area.
- Some scripts assume execution from specific working directories.
