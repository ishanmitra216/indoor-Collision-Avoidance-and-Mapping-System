import numpy as np

def transform_point(x, y, theta, distance):

    """
    Given robot pose (x, y, theta) and
    forward distance measurement,
    return world coordinates of obstacle
    """

    obs_x = x + distance * np.cos(theta)
    obs_y = y + distance * np.sin(theta)

    return obs_x, obs_y


def pose_matrix_to_xytheta(pose_matrix):

    x = pose_matrix[0, 3]
    y = pose_matrix[2, 3]

    theta = np.arctan2(
        pose_matrix[0, 2],
        pose_matrix[0, 0]
    )

    return x, y, theta