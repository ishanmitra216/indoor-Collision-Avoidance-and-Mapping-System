# db_config.py

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "robot.db")

DATABASE_URL = f"sqlite:///{DB_PATH}"