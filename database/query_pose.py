# query_pose.py

from db_manager import DBManager

class QueryPose:

    def __init__(self):
        self.db = DBManager()

    def get_latest(self):

        query = """
        SELECT x, y, theta, timestamp
        FROM pose
        ORDER BY id DESC
        LIMIT 1
        """

        return self.db.fetchone(query)

    def get_all(self):

        query = "SELECT x, y, theta, timestamp FROM pose"
        return self.db.fetchall(query)