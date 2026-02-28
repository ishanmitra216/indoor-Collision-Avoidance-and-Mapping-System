import numpy as np

def normalize_points(points):

    mean = np.mean(points, axis=0)
    std = np.std(points, axis=0)

    return (points - mean) / std