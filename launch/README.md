# Launch Module

This folder contains process orchestration scripts for starting and stopping
all major project services.

It supports:
- Cross-platform launching through Python.
- Unix shell helpers for Linux/macOS workflows.
- PowerShell wrappers for Windows.

## Main Component

### manage.py

Primary cross-platform launcher and stopper.

What it does:
- Starts all modules in sequence.
- Writes PID files into the launch folder.
- Stops running modules later using those PID files.

Supported commands:
- `python launch/manage.py start`
- `python launch/manage.py stop`

Start order in code:
1. Visual odometry (`visual_odometry/vo_main.py`)
2. Mapping (`mapping/grid_mapper.py`)
3. API (`uvicorn main:app` in api_server)
4. Dashboard (`python -m http.server 8080` in dashboard)

Stop behavior:
- Reads `vo.pid`, `mapping.pid`, `api.pid`, `dashboard.pid`.
- Uses `taskkill` on Windows and SIGTERM on Unix-like systems.
- Removes PID files after stopping.

## PowerShell Components (Windows)

### start_all.ps1

Wrapper script that calls:
- `python launch/manage.py start`

Use when:
- You want a simple Windows command to start everything.

### stop_all.ps1

Wrapper script that calls:
- `python launch/manage.py stop`

Use when:
- You want a simple Windows command to stop everything.

## Shell Components (Linux/macOS)

### start_all.sh

Unix helper that starts all modules in sequence by calling:
- `start_vo.sh`
- `start_mapping.sh`
- `start_api.sh`
- `start_dashboard.sh`

Includes short sleep delays between launches.

### stop_all.sh

Unix helper that:
- Reads and kills PIDs from local pid files.
- Removes pid files after stopping.

### start_vo.sh

Starts visual odometry process:
- Changes directory to visual_odometry.
- Runs `python3 vo_main.py` in background.
- Stores PID in `launch/vo.pid`.

### start_mapping.sh

Starts mapping process:
- Changes directory to mapping.
- Runs `python3 grid_mapper.py` in background.
- Stores PID in `launch/mapping.pid`.

### start_api.sh

Starts API server:
- Changes directory to api_server.
- Runs `uvicorn main:app --host 0.0.0.0 --port 8000 --reload` in background.
- Stores PID in `launch/api.pid`.

### start_dashboard.sh

Starts static dashboard server:
- Changes directory to dashboard.
- Runs `python3 -m http.server 8080` in background.
- Stores PID in `launch/dashboard.pid`.

## PID Files

Generated files:
- `vo.pid`
- `mapping.pid`
- `api.pid`
- `dashboard.pid`

These files are required for stop scripts to terminate the correct processes.

## Recommended Usage

For all platforms (recommended):

```bash
python launch/manage.py start
python launch/manage.py stop
```

Windows convenience:

```powershell
./launch/start_all.ps1
./launch/stop_all.ps1
```

Linux/macOS convenience:

```bash
bash launch/start_all.sh
bash launch/stop_all.sh
```

## Notes

- Run commands from the project root for consistent relative paths.
- If a service crashes, its PID file may remain and need manual cleanup.
- API is served on port `8000`, dashboard on port `8080`.
