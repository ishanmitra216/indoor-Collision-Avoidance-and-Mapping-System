import numpy as np
from occupancy_grid import OccupancyGrid
from coordinate_transform import transform_point

class GridMapper:

    def __init__(self):

        self.map = OccupancyGrid()
        self.last_pose = (0, 0, 0)

    def update_robot_pose(self, x, y, theta):

        self.last_pose = (x, y, theta)

        # Mark robot location as free
        self.map.set_free(x, y)

    def update_obstacle(self, distance):

        x, y, theta = self.last_pose

        if distance <= 0:
            return

        obs_x, obs_y = transform_point(x, y, theta, distance)

        # Mark obstacle cell
        self.map.set_occupied(obs_x, obs_y)

    def get_map(self):

        return self.map.get_grid()

    def save_map(self, filename="saved_maps/map1.npy"):

        np.save(filename, self.map.get_grid())

    def load_map(self, filename="saved_maps/map1.npy"):

        self.map.grid = np.load(filename)