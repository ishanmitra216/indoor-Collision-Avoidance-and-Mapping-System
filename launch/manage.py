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
LOG_DIR = os.path.join(LAUNCH_DIR, "logs")


def write_pid(name, pid):
    path = os.path.join(LAUNCH_DIR, f"{name}.pid")
    with open(path, "w") as f:
        f.write(str(pid))


def remove_pid(name):
    path = os.path.join(LAUNCH_DIR, f"{name}.pid")
    try:
        os.remove(path)
    except OSError:
        pass


def start_process(label, cmd, cwd):
    os.makedirs(LOG_DIR, exist_ok=True)
    log_path = os.path.join(LOG_DIR, f"{label}.log")
    log_file = open(log_path, "a")

    kwargs = {
        "cwd": cwd,
        "stdout": log_file,
        "stderr": subprocess.STDOUT,
    }
    if os.name == 'nt':
        kwargs["creationflags"] = subprocess.CREATE_NEW_PROCESS_GROUP
    else:
        kwargs["start_new_session"] = True

    proc = subprocess.Popen(cmd, **kwargs)
    log_file.close()
    time.sleep(1)
    if proc.poll() is not None:
        remove_pid(label)
        print(f"{label} failed to start (exit code {proc.returncode}). Check log: {log_path}")
        return None

    write_pid(label, proc.pid)
    print(f"{label} started with PID {proc.pid} (log: {log_path})")
    return proc


def _pid_running(pid):
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def _prune_dead_pids():
    for name in ['vo', 'mapping', 'api', 'dashboard']:
        pidfile = os.path.join(LAUNCH_DIR, f"{name}.pid")
        if not os.path.exists(pidfile):
            continue
        try:
            with open(pidfile) as f:
                pid = int(f.read().strip())
        except (OSError, ValueError):
            remove_pid(name)
            continue

        if not _pid_running(pid):
            remove_pid(name)
            print(f"{name} exited shortly after startup; removed stale PID file.")


def start_all():
    print("Starting all modules...")
    procs = {}
    os.chdir(ROOT_DIR)  # ensure paths are relative to repo root

    for name in ['vo', 'mapping', 'api', 'dashboard']:
        remove_pid(name)

    procs['vo'] = start_process('vo', [sys.executable, 'vo_main.py'], os.path.join(ROOT_DIR, 'visual_odometry'))
    time.sleep(2)

    procs['mapping'] = start_process('mapping', [sys.executable, 'mapping_main.py'], os.path.join(ROOT_DIR, 'mapping'))
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
    # Give short-lived processes (for example camera-dependent VO in headless envs)
    # enough time to exit before pruning stale PID files.
    time.sleep(3)
    _prune_dead_pids()

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
