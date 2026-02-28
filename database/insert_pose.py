# insert_pose.py

from db_manager import DBManager
from models import PoseModel
import datetime

class InsertPose:

    def __init__(self):
        self.db = DBManager()

    def insert(self, pose: PoseModel):

        query = """
        INSERT INTO pose (x, y, theta, timestamp)
        VALUES (?, ?, ?, ?)
        """

        timestamp = pose.timestamp or datetime.datetime.now()

        self.db.execute(query, (pose.x, pose.y, pose.theta, timestamp))