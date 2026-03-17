# ROS Workspace Module

This folder contains the ROS catkin workspace used to run the JetBot indoor
navigation stack as ROS nodes.

## Workspace Structure

- `src/`
	- Source space for ROS package code, launch files, messages, and configs.
- `build/`
	- Catkin build artifacts (generated after build).
- `devel/`
	- Development environment outputs, setup scripts, and generated files.
- `logs/`
	- Build and runtime logs.

In the current workspace snapshot, `build/`, `devel/`, and `logs/` are empty.

## Source Components (`src/`)

### Package Metadata

- `src/jetbot_navigation/package.xml`
	- Declares package name/version/maintainer/license.
	- Lists ROS dependencies such as `rospy`, `sensor_msgs`, `geometry_msgs`,
		`nav_msgs`, `cv_bridge`, and `tf`.

- `src/jetbot_navigation/CMakeLists.txt`
	- Catkin build configuration.
	- Registers custom message files:
		- `Pose.msg`
		- `Map.msg`
		- `Obstacle.msg`
	- Enables message generation/runtime.
	- Installs Python node scripts into catkin package bin destination.

### Message Definitions (`src/msg/`)

- `src/msg/Pose.msg`
	- Fields: `x`, `y`, `theta`.
	- Used for robot pose publishing/subscribing.

- `src/msg/Map.msg`
	- Fields: `width`, `height`, `data`.
	- Generic map container message format.

- `src/msg/Obstacle.msg`
	- Fields: `detected`, `distance`.
	- Used by collision pipeline and motor control.

### Launch Files (`src/launch/`)

- `src/launch/camera.launch`
	- Launches `camera_node.py` only.

- `src/launch/mapping.launch`
	- Launches `mapping_node.py` only.

- `src/launch/navigation.launch`
	- Launches `vo_node.py` and `collision_node.py`.

- `src/launch/full_system.launch`
	- Launches complete stack:
		- camera node
		- visual odometry node
		- mapping node
		- collision node
		- motor node
		- database node
		- tf node

### Runtime Nodes (`src/nodes/`)

- `src/nodes/camera_node.py`
	- Captures frames from camera index 0 using OpenCV.
	- Publishes images to `/camera/image_raw` as ROS `sensor_msgs/Image`.

- `src/nodes/vo_node.py`
	- Subscribes to `/camera/image_raw`.
	- Runs ORB feature detection/matching and essential-matrix pose recovery.
	- Publishes estimated pose to `/robot/pose` using custom `Pose` message.

- `src/nodes/mapping_node.py`
	- Subscribes to `/robot/pose`.
	- Updates a simple 200x200 occupancy grid.
	- Publishes ROS `nav_msgs/OccupancyGrid` on `/map`.

- `src/nodes/collision_node.py`
	- Subscribes to `/camera/image_raw`.
	- Uses center-region brightness heuristic to detect obstacle presence.
	- Publishes `Obstacle` message on `/collision_status`.

- `src/nodes/motor_node.py`
	- Subscribes to `/collision_status`.
	- Stops JetBot when obstacle is detected, otherwise drives forward.

- `src/nodes/database_node.py`
	- Subscribes to `/robot/pose`.
	- Creates and writes pose records into SQLite database.

- `src/nodes/tf_node.py`
	- Subscribes to `/robot/pose`.
	- Broadcasts `map -> base_link` transform using ROS TF.

### Configuration Files (`src/config/`)

- `src/config/camera.yaml`
	- Camera intrinsic-related values (`focal_length`, `cx`, `cy`).

- `src/config/mapping.yaml`
	- Mapping size and resolution parameters.

- `src/config/navigation.yaml`
	- Navigation motion and obstacle threshold settings.

### Utility Script (`src/scripts/`)

- `src/scripts/startup.sh`
	- Sources workspace setup file from `devel/setup.bash`.
	- Launches full ROS system with `roslaunch jetbot_navigation full_system.launch`.

## Topic/Data Flow Summary

1. `camera_node` publishes `/camera/image_raw`.
2. `vo_node` consumes camera frames and publishes `/robot/pose`.
3. `mapping_node` consumes pose and publishes `/map`.
4. `collision_node` consumes camera frames and publishes `/collision_status`.
5. `motor_node` consumes collision status and drives/stops robot.
6. `database_node` logs pose to SQLite.
7. `tf_node` publishes transform for ROS visualization/integration.

## Build and Run Notes

- Build workspace with catkin tools (for example `catkin_make`) from
	`ros_workspace`.
- Source `devel/setup.bash` before launching nodes.
- Use launch files for selective modules, or `full_system.launch` for full run.
