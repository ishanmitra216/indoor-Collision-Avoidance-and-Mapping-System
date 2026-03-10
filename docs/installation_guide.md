# Installation Guide

## 1. Flash Jetson Nano

Install JetPack 4.6 (Ubuntu 18.04)

## 2. Install ROS Melodic

sudo apt install ros-melodic-desktop-full

## 3. Clone Project

git clone <repo>

## 4. Run Setup

The repository includes both a shell script (`setup.sh`) and a
cross-platform Python helper (`setup.py`).

* **Linux / macOS** – run `bash setup.sh` or `python3 setup.py`.
* **Windows** – open PowerShell or Command Prompt and execute:
  ```
  py setup.py
  ```

The Python version works consistently across operating systems.

## 5. Launch System

Two launch mechanisms are provided:

* **ROS launch** (when running on a Jetson Nano with ROS installed):
  ```
  roslaunch jetbot_navigation full_system.launch
  ```
* **Python launcher** (cross-platform, starts all four modules):
  ```
  python launch/manage.py start
  ```
  Use `python launch/manage.py stop` to shut the modules down later.  On
  Windows you can also run `launch\start_all.ps1` and
  `launch\stop_all.ps1` from PowerShell instead of invoking Python directly.

### GUI control panel
If you prefer buttons instead of commands, run the Tkinter GUI:

```bash
python gui/app.py
```

It works on any OS with a display.

### Containerized operation
The repo includes Docker support for isolated deployment.

* **Single container** – build the root Dockerfile:
  ```bash
  docker build -t indoor-nav .
  docker run -it --rm -p 8000:8000 -p 8080:8080 indoor-nav
  ```
* **Multiple services** – use compose:
  ```bash
  docker-compose up --build
  ```
  A `gui` service is included but requires X11/Wayland forwarding or
  host networking.

Ports and device mappings can be adjusted to match your environment.

Windows users should invoke `py` instead of `python` if necessary.

> **GUI prerequisite:** the Tkinter library is part of the standard Python
> distribution, but some Linux packages (e.g. Debian/Ubuntu) ship it separately
> as `python3-tk`.  Install that package before running `python gui/app.py`.

## 6. Start API

uvicorn main:app --reload