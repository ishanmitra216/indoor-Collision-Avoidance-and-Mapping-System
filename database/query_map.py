# query_map.py

import numpy as np
from db_manager import DBManager

class QueryMap:

    def __init__(self):
        self.db = DBManager()

    def get_latest(self):

        query = """
        SELECT width, height, data
        FROM map
        ORDER BY id DESC
        LIMIT 1
        """

        result = self.db.fetchone(query)

        if result:
            width, height, data_bytes = result
            grid = np.frombuffer(data_bytes, dtype=np.int8)
            grid = grid.reshape((height, width))
            return grid

        return None