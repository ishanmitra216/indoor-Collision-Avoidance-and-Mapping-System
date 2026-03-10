#!/usr/bin/env python3
"""Cross-platform launcher for the Indoor Collision Avoidance project.

Usage from the repository root:

    python launch/manage.py start   # start all modules
    python launch/manage.py stop    # stop previously started modules

The script mirrors the behavior of the original shell scripts but works on
Windows, macOS, and Linux.  PID files are written into the `launch/` directory
just like the shell helpers used to.
"""

import os
import subprocess
import sys
import time
import signal

LAUNCH_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(LAUNCH_DIR, os.pardir))


def write_pid(name, pid):
    path = os.path.join(LAUNCH_DIR, f"{name}.pid")
    with open(path, "w") as f:
        f.write(str(pid))


def start_process(label, cmd, cwd):
    proc = subprocess.Popen(cmd, cwd=cwd)
    write_pid(label, proc.pid)
    print(f"{label} started with PID {proc.pid}")
    return proc


def start_all():
    print("Starting all modules...")
    procs = {}
    os.chdir(ROOT_DIR)  # ensure paths are relative to repo root

    procs['vo'] = start_process('vo', [sys.executable, 'vo_main.py'], os.path.join(ROOT_DIR, 'visual_odometry'))
    time.sleep(2)

    procs['mapping'] = start_process('mapping', [sys.executable, 'grid_mapper.py'], os.path.join(ROOT_DIR, 'mapping'))
    time.sleep(2)

    procs['api'] = start_process(
        'api',
        [sys.executable, '-m', 'uvicorn', 'main:app', '--host', '0.0.0.0', '--port', '8000', '--reload'],
        os.path.join(ROOT_DIR, 'api_server'),
    )
    time.sleep(2)

    procs['dashboard'] = start_process(
        'dashboard',
        [sys.executable, '-m', 'http.server', '8080'],
        os.path.join(ROOT_DIR, 'dashboard'),
    )
    print("All modules launched.  Use Ctrl-C to quit or run `python launch/manage.py stop` later.")
    return procs


def stop_all():
    print("Stopping all services...")
    for name in ['vo', 'mapping', 'api', 'dashboard']:
        pidfile = os.path.join(LAUNCH_DIR, f"{name}.pid")
        if os.path.exists(pidfile):
            with open(pidfile) as f:
                pid = int(f.read().strip())
            try:
                if os.name == 'nt':
                    subprocess.check_call(['taskkill', '/PID', str(pid), '/F'])
                else:
                    os.kill(pid, signal.SIGTERM)
                print(f"{name} (pid {pid}) stopped")
            except Exception as e:
                print(f"failed to stop {name}: {e}")
            try:
                os.remove(pidfile)
            except OSError:
                pass
        else:
            print(f"no pid file for {name}")
    print("All services stopped.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python launch/manage.py [start|stop]")
        sys.exit(1)
    cmd = sys.argv[1].lower()
    if cmd == 'start':
        start_all()
    elif cmd == 'stop':
        stop_all()
    else:
        print("Unknown command", cmd)
        sys.exit(1)


if __name__ == '__main__':
    main()
