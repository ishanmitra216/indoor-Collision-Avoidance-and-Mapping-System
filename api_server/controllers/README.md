# Controllers Directory

This folder contains the *controller* functions used by the API layer to fetch
and shape data coming from services before sending it back to clients.  Each
controller corresponds to one or more FastAPI route modules defined in
`api_server/routes`.

Controllers are intentionally thin: they do not perform business logic or
access the database directly.  Instead they import and invoke the appropriate
service classes from `api_server/services` (e.g. `DBService`,
`RobotService`), then transform the returned values into JSON-friendly Python
objects.

## Files

- **`map_controller.py`** – retrieves the most recent occupancy map from the
  database.  The raw bytes are Base64-encoded and the width/height are
  included so that the dashboard or other clients can reconstruct the map.

- **`pose_controller.py`** – fetches the latest robot pose (x, y, theta,
  timestamp) and returns it as a dictionary.  If no pose is available a simple
  error message is returned instead.

- **`robot_controller.py`** – exposes two small wrappers around
  `RobotService` (state and collision status).  These are used by the
  `/robot/state` and `/collision/status` endpoints.

Additional controllers can be added as new features are introduced; keep the
same pattern of delegating to a service and formatting the result.

## Usage

Controllers are imported and called from the FastAPI router files.  For
example, `api_server/routes/map.py` defines a `GET /map/latest` endpoint that
calls `map_controller.get_latest_map()`.

All controllers are synchronous and return native Python dictionaries or
objects that FastAPI will automatically convert to JSON.  Exceptions and error
handling are kept minimal here – more complex validation should occur in the
service layer or in Pydantic models at the route level.

> ⚠️ **Note:** Keep controllers lightweight to preserve separation of
> concerns. Business rules belong in `services/` and data models belong in
> `models/`.
