import sqlite3
from config import DATABASE_URL

class DBService:

    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_URL, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def get_latest_pose(self):

        query = """
        SELECT x, y, theta, timestamp
        FROM pose
        ORDER BY id DESC
        LIMIT 1
        """

        return self.cursor.execute(query).fetchone()

    def get_latest_map(self):

        query = """
        SELECT width, height, data
        FROM map
        ORDER BY id DESC
        LIMIT 1
        """

        return self.cursor.execute(query).fetchone()