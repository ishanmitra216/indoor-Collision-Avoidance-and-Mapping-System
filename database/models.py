# models.py

class PoseModel:

    def __init__(self, x, y, theta, timestamp=None):
        self.x = x
        self.y = y
        self.theta = theta
        self.timestamp = timestamp


class MapModel:

    def __init__(self, width, height, data, timestamp=None):
        self.width = width
        self.height = height
        self.data = data
        self.timestamp = timestamp