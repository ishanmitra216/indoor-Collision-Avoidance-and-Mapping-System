class CameraModel:

    def __init__(self):

        self.focal = 718.8560
        self.cx = 320
        self.cy = 240

        self.principal_point = (self.cx, self.cy)

    def get_matrix(self):

        return [
            [self.focal, 0, self.cx],
            [0, self.focal, self.cy],
            [0, 0, 1]
        ]