import os
import importlib.util
import subprocess
import sys


def test_gui_script_exists_and_importable():
    path = os.path.join(os.path.dirname(__file__), os.pardir, "gui", "app.py")
    assert os.path.isfile(path), "GUI script is missing"
    # try importing without running mainloop
    spec = importlib.util.spec_from_file_location("gui_app", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert hasattr(module, "ControllerGUI"), "ControllerGUI class not found in gui/app.py"


def test_docker_files_present():
    root = os.path.dirname(os.path.dirname(__file__))
    assert os.path.isfile(os.path.join(root, "Dockerfile")), "Dockerfile missing"
    assert os.path.isfile(os.path.join(root, "docker-compose.yml")), "docker-compose.yml missing"


# This test ensures that the Python launcher can be invoked with --help
# without actually starting all processes, which would be disruptive in CI.
def test_python_launcher_help():
    root = os.path.dirname(os.path.dirname(__file__))
    launcher = os.path.join(root, "launch", "manage.py")
    result = subprocess.run([sys.executable, launcher, "--help"], capture_output=True, text=True)
    assert result.returncode == 0, f"launcher returned {result.returncode}, stderr: {result.stderr}"
