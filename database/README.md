# Database Module

This folder contains the local SQLite data layer used to store and retrieve
robot pose and occupancy map data.

## Purpose

- Define database connection and helpers.
- Define lightweight data models for insert operations.
- Insert and query pose/map records.
- Initialize database tables from SQL schema files.

## File Components

### db_config.py

Configuration for database location and SQLAlchemy-style URL.

Contains:
- `BASE_DIR`: absolute path of the database folder.
- `DB_PATH`: path to local SQLite file `robot.db`.
- `DATABASE_URL`: SQLite URL string (`sqlite:///...`) for integrations that
	require URL format.

### db_manager.py

Core database utility wrapper around sqlite3.

Contains class `DBManager` with:
- `__init__()`: opens SQLite connection (`check_same_thread=False`) and cursor.
- `execute(query, params=())`: executes write query and commits.
- `fetchall(query, params=())`: returns all rows.
- `fetchone(query, params=())`: returns single row.
- `close()`: closes connection.

### models.py

Simple Python container models used by insert scripts.

Contains:
- `PoseModel(x, y, theta, timestamp=None)`
- `MapModel(width, height, data, timestamp=None)`

Note:
- `MapModel.data` is expected to be a NumPy array before serialization.

### insert_pose.py

Write helper for pose records.

Contains class `InsertPose`:
- Creates a `DBManager` instance.
- `insert(pose: PoseModel)` inserts into `pose` table.
- Uses provided timestamp or current datetime if missing.

### insert_map.py

Write helper for map records.

Contains class `InsertMap`:
- Creates a `DBManager` instance.
- `insert(map_model: MapModel)` inserts into `map` table.
- Converts NumPy map grid to bytes using `tobytes()`.
- Uses provided timestamp or current datetime if missing.

### query_pose.py

Read helper for pose records.

Contains class `QueryPose`:
- `get_latest()`: fetches newest pose row by descending id.
- `get_all()`: fetches all pose rows.

Returns raw tuples from sqlite cursor.

### query_map.py

Read helper for map records.

Contains class `QueryMap`:
- `get_latest()`: fetches latest `(width, height, data)` from `map` table.
- Reconstructs NumPy grid from BLOB with `np.frombuffer(..., dtype=np.int8)`.
- Reshapes data into `(height, width)` and returns grid.
- Returns `None` if no map row exists.

### migrations/init_db.py

Database bootstrap script.

What it does:
- Loads SQL from schema files in `database/schemas`.
- Executes scripts using `executescript`.
- Creates tables if they do not already exist.

Run directly to initialize DB structure.

### schemas/pose_schema.sql

Defines `pose` table:
- `id` primary key autoincrement
- `x`, `y`, `theta` as required REAL columns
- `timestamp` with default current timestamp

### schemas/map_schema.sql

Defines `map` table:
- `id` primary key autoincrement
- `width`, `height` as required INTEGER columns
- `data` as required BLOB column
- `timestamp` with default current timestamp

## Typical Data Flow

1. Mapping/VO pipeline creates `PoseModel` or `MapModel`.
2. Insert class stores row in SQLite through `DBManager`.
3. API layer queries latest rows with `QueryPose` or `QueryMap` patterns.
4. Map BLOB is reconstructed to NumPy grid or encoded for API response.

## Quick Usage

Initialize database tables:

```bash
python database/migrations/init_db.py
```

Insert and query are typically called by other project modules rather than
manually from CLI.
