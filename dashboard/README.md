# Dashboard Module

This folder contains the frontend pages and JavaScript logic that visualize
data served by the API server.

Important clarification:
- There are no JavaScript files inside api_server.
- JavaScript files are in dashboard/js and call API endpoints from api_server.

## JavaScript Components

### js/api.js

Shared API helper layer.

What it contains:
- API base URL: localhost on port 8000.
- Reusable async function `fetchData(endpoint)` that:
	- Sends an HTTP request with fetch.
	- Parses and returns JSON response.

Role in system:
- Centralizes all network calls so other JS files only pass endpoint paths.

### js/map.js

Map rendering logic for latest occupancy grid.

What it does:
- Calls `/map/latest` through `fetchData`.
- Reads `width`, `height`, and `map_data_base64` from API response.
- Decodes Base64 bytes into a typed array.
- Converts occupancy values to grayscale pixels on a canvas:
	- 100 -> black (occupied)
	- 0 -> white (free)
	- other -> gray (unknown)
- Draws result into element with id mapCanvas.

Role in system:
- Turns raw map bytes from the backend into a visible occupancy map.

### js/pose.js

Pose panel update logic.

What it does:
- Calls `/pose/latest` through `fetchData`.
- Injects returned pose values into element with id pose-data:
	- x
	- y
	- theta
	- timestamp

Role in system:
- Displays current robot pose received from API server.

### js/visualization.js

Robot state and collision status visualization logic.

What it does:
- `updateRobotState()`:
	- Calls `/robot/state`.
	- Writes x, y, theta, and status into element with id robot-state.
- `updateCollisionStatus()`:
	- Calls `/collision/status`.
	- Writes detected and distance into element with id collision-status.

Role in system:
- Shows live operational and safety indicators on dashboard.

## Endpoint Mapping (JS -> API Server)

- `js/map.js` -> `/map/latest`
- `js/pose.js` -> `/pose/latest`
- `js/visualization.js` -> `/robot/state`, `/collision/status`
- `js/api.js` -> shared helper used by all files above

## Data Flow

1. Browser page loads dashboard scripts.
2. Script calls `fetchData` with endpoint path.
3. API server returns JSON.
4. Script updates canvas or HTML elements.
5. User sees current map, pose, robot state, and collision status.
