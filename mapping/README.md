# Mapping Module

This module builds and maintains a 2D occupancy grid map from robot pose and
obstacle distance observations.

## Purpose

- Convert robot/world coordinates into grid cells.
- Mark free and occupied cells in an occupancy grid.
- Save, load, and visualize map outputs.

## File Components

### occupancy_grid.py

Defines the core map container: `OccupancyGrid`.

Key responsibilities:
- Initializes a grid with unknown state (`-1`).
- Stores map metadata:
	- `width` (default `400`)
	- `height` (default `400`)
	- `resolution` in meters/cell (default `0.05`)
- Uses centered origin (`origin_x`, `origin_y`) so world `(0,0)` is near map center.

Main methods:
- `world_to_grid(x, y)`: converts world coordinates to integer grid indices.
- `set_occupied(x, y)`: writes occupancy value `100` if within bounds.
- `set_free(x, y)`: writes free-space value `0` if within bounds.
- `get_grid()`: returns the NumPy grid.

Cell encoding:
- `-1` = unknown
- `0` = free
- `100` = occupied

### coordinate_transform.py

Coordinate utility functions used by mapping updates.

Functions:
- `transform_point(x, y, theta, distance)`:
	- Projects a forward obstacle measurement from robot pose into world space.
	- Returns obstacle world coordinates `(obs_x, obs_y)`.
- `pose_matrix_to_xytheta(pose_matrix)`:
	- Converts a 4x4 pose transform matrix into `(x, y, theta)`.
	- Extracts translation and yaw estimate from matrix elements.

### grid_mapper.py

High-level mapping orchestrator: `GridMapper`.

Key responsibilities:
- Owns an `OccupancyGrid` instance.
- Tracks latest robot pose as `(x, y, theta)`.
- Updates map with robot free-space and obstacle hits.

Main methods:
- `update_robot_pose(x, y, theta)`:
	- Stores last robot pose.
	- Marks robot cell as free.
- `update_obstacle(distance)`:
	- Ignores invalid non-positive distances.
	- Computes obstacle world point via `transform_point`.
	- Marks corresponding grid cell as occupied.
- `get_map()`: returns current grid.
- `save_map(filename="saved_maps/map1.npy")`: saves grid as NumPy `.npy`.
- `load_map(filename="saved_maps/map1.npy")`: loads grid from `.npy`.

### map_visualizer.py

Map rendering and export utilities.

Functions:
- `visualize_map(grid)`:
	- Converts occupancy values to grayscale image.
	- Resizes image to `600x600` for display.
	- Shows live OpenCV window (`cv2.imshow`).
- `save_map_png(grid, filename="saved_maps/map.png")`:
	- Ensures `saved_maps` directory exists.
	- Converts grid to grayscale image.
	- Saves PNG snapshot to disk.

Color mapping in visualization:
- unknown (`-1`) -> gray
- free (`0`) -> white
- occupied (`100`) -> black

## Typical Mapping Flow

1. Pose source provides `(x, y, theta)`.
2. Call `GridMapper.update_robot_pose(...)`.
3. Sensor/avoidance module provides obstacle distance.
4. Call `GridMapper.update_obstacle(distance)`.
5. Retrieve map with `get_map()`.
6. Display via `visualize_map(...)` or persist with `save_map(...)`/`save_map_png(...)`.

## Integration Notes

- `GridMapper` expects distance measured in the same metric units used by map
	resolution and pose coordinates.
- `pose_matrix_to_xytheta` supports pipelines that output 4x4 transforms
	(for example visual odometry outputs).
- Map persistence default path is `mapping/saved_maps/map1.npy`.

---

## New: mapping_main.py – Long-Running Service Entrypoint

Added `mapping_main.py` as the process-level entrypoint used by the launcher.
`grid_mapper.py` is a **library module** and exits immediately when run directly;
`mapping_main.py` wraps it in a run-loop and is what `launch/manage.py` and
`launch/start_mapping.sh` now invoke.

What it does:
- Initializes a `GridMapper` with the robot at origin `(0, 0, 0)`.
- Handles `SIGTERM` / `SIGINT` for clean shutdown.
- Writes a live map snapshot to `saved_maps/map_live.npy` every second.
- Runs until stopped by `launch/manage.py stop` or Ctrl-C.

Run standalone (from repo root):

```bash
.venv/bin/python mapping/mapping_main.py
```

Live map output: `mapping/saved_maps/map_live.npy`
