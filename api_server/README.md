# API Server

This module exposes a small FastAPI service for the indoor navigation stack.
It serves the latest pose/map data and basic robot/collision status endpoints
used by the dashboard and other clients.

## What This Service Does

- Starts a FastAPI app for JetBot navigation APIs.
- Reads latest pose and map records from the SQLite database.
- Returns robot state and collision status from an in-memory service.

## Directory Layout

```text
api_server/
	config.py
	main.py
	controllers/
		map_controller.py
		pose_controller.py
		robot_controller.py
	models/
		map_model.py
		pose_model.py
	routes/
		collision.py
		map.py
		pose.py
		robot.py
	services/
		db_service.py
		robot_service.py
```

## File Explanation

### Top-Level Files

- `main.py`
	- Application entry point.
	- Creates `FastAPI(title="JetBot Navigation API")`.
	- Registers routers from `routes/pose.py`, `routes/map.py`,
		`routes/collision.py`, and `routes/robot.py`.
	- Defines health/root endpoint: `GET /`.

- `config.py`
	- Builds `BASE_DIR` and SQLite `DB_PATH`.
	- Exposes `DATABASE_URL`, `API_HOST`, and `API_PORT`.
	- Used by `services/db_service.py` for database connection setup.

### Routes Layer (`routes/`)

Each route file defines URL paths and delegates to a controller.

- `routes/pose.py`
	- Prefix: `/pose`
	- Endpoint: `GET /pose/latest`
	- Calls: `controllers.pose_controller.get_latest_pose()`

- `routes/map.py`
	- Prefix: `/map`
	- Endpoint: `GET /map/latest`
	- Calls: `controllers.map_controller.get_latest_map()`

- `routes/robot.py`
	- Prefix: `/robot`
	- Endpoint: `GET /robot/state`
	- Calls: `controllers.robot_controller.get_robot_state()`

- `routes/collision.py`
	- Prefix: `/collision`
	- Endpoint: `GET /collision/status`
	- Calls: `controllers.robot_controller.get_collision_status()`

### Controllers Layer (`controllers/`)

Controllers shape response payloads and call services.

- `controllers/pose_controller.py`
	- Uses `DBService` to fetch latest pose row.
	- Returns `{x, y, theta, timestamp}` when data exists.
	- Returns `{"message": "No pose data available"}` when empty.

- `controllers/map_controller.py`
	- Uses `DBService` to fetch latest map row.
	- Base64-encodes binary map bytes before returning JSON.
	- Returns `{width, height, map_data_base64}`.
	- Returns `{"message": "No map data available"}` when empty.

- `controllers/robot_controller.py`
	- Uses `RobotService` singleton-style instance.
	- Returns in-memory robot state and collision status.

### Services Layer (`services/`)

Services handle data access or state storage.

- `services/db_service.py`
	- Opens SQLite connection to `DATABASE_URL`.
	- `get_latest_pose()` queries newest pose (`ORDER BY id DESC LIMIT 1`).
	- `get_latest_map()` queries newest map (`ORDER BY id DESC LIMIT 1`).

- `services/robot_service.py`
	- Maintains in-memory dictionaries for robot and collision state.
	- Exposes update methods:
		- `update_state(x, y, theta, status)`
		- `update_collision(detected, distance)`
	- Exposes read methods:
		- `get_state()`
		- `get_collision_status()`

### Models Layer (`models/`)

Pydantic response models (currently not directly wired to route decorators,
but available for validation and OpenAPI typing if needed).

- `models/pose_model.py`
	- `PoseResponse`: `x`, `y`, `theta`, `timestamp`

- `models/map_model.py`
	- `MapResponse`: `width`, `height`, `map_data_base64`

## API Summary

- `GET /` -> service status message
- `GET /pose/latest` -> latest robot pose from DB
- `GET /map/latest` -> latest occupancy map from DB (Base64)
- `GET /robot/state` -> current in-memory robot state
- `GET /collision/status` -> current in-memory collision state

## Typical Data Flow

1. Client hits a route endpoint.
2. Route calls controller function.
3. Controller calls service function.
4. Service fetches state/data (DB or memory).
5. Controller formats response as JSON-friendly dict.

## Run (Example)

From project root:

```bash
uvicorn api_server.main:app --host 0.0.0.0 --port 8000 --reload
```

Then open:

- `http://localhost:8000/`
- `http://localhost:8000/docs`

## Notes

- `DBService` keeps one SQLite connection per service instance.
- Map data is sent as Base64 to safely transport binary map bytes in JSON.
- If you want stricter schema validation in responses, attach
	`response_model=PoseResponse` and `response_model=MapResponse` in route
	decorators.
