import os

def create_dir(path):

    if not os.path.exists(path):
        os.makedirs(path)

def save_trajectory(path, positions):

    with open(path, "w") as f:
        for p in positions:
            f.write(f"{p[0]} {p[1]}\n")