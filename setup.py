#!/usr/bin/env python3
"""Cross-platform setup helper.

Replaces the original `setup.sh` with a Python-based installer that works on
Windows, Linux, or macOS.  It installs Python dependencies, attempts to build
the ROS workspace if `catkin_make` is available, and initializes the SQLite
database.
"""

import os
import subprocess
import sys


def run(cmd, cwd=None):
    print("Running:", cmd, "in", cwd or os.getcwd())
    subprocess.check_call(cmd, cwd=cwd)


def install_requirements():
    req_file = os.path.join(os.getcwd(), "requirements.txt")
    if not os.path.exists(req_file):
        print("requirements.txt not found, skipping dependency installation.")
        return

    try:
        import pip  # noqa: F401
    except ImportError:
        try:
            run([sys.executable, "-m", "ensurepip", "--upgrade"])
        except subprocess.CalledProcessError:
            print("pip is not available and could not be bootstrapped; skipping dependency installation.")
            return

    try:
        run([sys.executable, "-m", "pip", "install", "-r", req_file])
    except subprocess.CalledProcessError:
        print("Dependency installation failed; continuing setup so other steps can run.")


def setup_ros_workspace():
    ros_dir = os.path.join(os.getcwd(), "ros_workspace")
    if not os.path.isdir(ros_dir):
        print("ROS workspace directory not present, skipping ROS setup.")
        return
    # only attempt if catkin_make is available
    try:
        run(["catkin_make"], cwd=ros_dir)
        print("Source the workspace with: source %s/devel/setup.bash" % ros_dir)
    except FileNotFoundError:
        print("`catkin_make` not found; skipping ROS workspace build.")
    except subprocess.CalledProcessError:
        print("ROS workspace build failed; you may need to install ROS or fix the workspace.")


def init_database():
    migration_dir = os.path.join(os.getcwd(), "database", "migrations")
    if not os.path.isdir(migration_dir):
        print("Database migration directory missing, skipping DB initialization.")
        return
    run([sys.executable, "init_db.py"], cwd=migration_dir)


def main():
    print("=== Setup starting ===")
    install_requirements()
    setup_ros_workspace()
    init_database()
    print("=== Setup completed successfully ===")


if __name__ == "__main__":
    main()
