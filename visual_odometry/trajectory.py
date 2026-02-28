import numpy as np

class Trajectory:

    def __init__(self):
        self.positions = []

    def update(self, pose):

        x = pose[0,3]
        y = pose[2,3]

        self.positions.append((x, y))

    def get_positions(self):
        return np.array(self.positions)