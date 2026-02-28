import numpy as np
import cv2

traj_img = np.zeros((600, 600, 3), dtype=np.uint8)

def draw_trajectory(positions):

    global traj_img

    for pos in positions:

        x, y = pos

        draw_x = int(x) + 300
        draw_y = int(y) + 100

        cv2.circle(traj_img, (draw_x, draw_y), 1, (0,255,0), 2)

    cv2.imshow("Trajectory", traj_img)