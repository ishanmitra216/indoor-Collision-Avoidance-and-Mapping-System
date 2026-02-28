# config.py

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "../database/robot.db")

DATABASE_URL = DB_PATH
API_HOST = "0.0.0.0"
API_PORT = 8000