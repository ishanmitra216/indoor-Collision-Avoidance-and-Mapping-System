# db_manager.py

import sqlite3
from db_config import DB_PATH

class DBManager:

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()