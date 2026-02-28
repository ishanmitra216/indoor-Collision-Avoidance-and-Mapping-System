import cv2
import numpy as np
import os

def visualize_map(grid):

    # Convert grid values to image
    img = np.zeros_like(grid, dtype=np.uint8)

    img[grid == -1] = 127   # Unknown → Gray
    img[grid == 0] = 255    # Free → White
    img[grid == 100] = 0    # Occupied → Black

    img = cv2.resize(img, (600, 600))

    cv2.imshow("Occupancy Grid Map", img)
    cv2.waitKey(1)


def save_map_png(grid, filename="saved_maps/map.png"):

    if not os.path.exists("saved_maps"):
        os.makedirs("saved_maps")

    img = np.zeros_like(grid, dtype=np.uint8)

    img[grid == -1] = 127
    img[grid == 0] = 255
    img[grid == 100] = 0

    cv2.imwrite(filename, img)