# insert_map.py

import numpy as np
import datetime
from db_manager import DBManager
from models import MapModel

class InsertMap:

    def __init__(self):
        self.db = DBManager()

    def insert(self, map_model: MapModel):

        # Convert numpy array to bytes
        map_bytes = map_model.data.tobytes()

        query = """
        INSERT INTO map (width, height, data, timestamp)
        VALUES (?, ?, ?, ?)
        """

        timestamp = map_model.timestamp or datetime.datetime.now()

        self.db.execute(
            query,
            (map_model.width, map_model.height, map_bytes, timestamp)
        )