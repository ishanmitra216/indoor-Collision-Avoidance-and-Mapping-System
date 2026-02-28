import numpy as np

class OccupancyGrid:

    def __init__(self, width=400, height=400, resolution=0.05):

        self.width = width
        self.height = height
        self.resolution = resolution

        # Initialize grid with unknown cells (-1)
        self.grid = np.ones((height, width), dtype=np.int8) * -1

        # Center of grid
        self.origin_x = width // 2
        self.origin_y = height // 2

    def world_to_grid(self, x, y):

        gx = int(x / self.resolution) + self.origin_x
        gy = int(y / self.resolution) + self.origin_y

        return gx, gy

    def set_occupied(self, x, y):

        gx, gy = self.world_to_grid(x, y)

        if 0 <= gx < self.width and 0 <= gy < self.height:
            self.grid[gy, gx] = 100

    def set_free(self, x, y):

        gx, gy = self.world_to_grid(x, y)

        if 0 <= gx < self.width and 0 <= gy < self.height:
            self.grid[gy, gx] = 0

    def get_grid(self):
        return self.grid