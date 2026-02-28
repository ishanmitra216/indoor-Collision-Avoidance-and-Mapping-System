from database.insert_pose import InsertPose
from database.models import PoseModel

pose = PoseModel(1.0, 2.0, 0.0)

InsertPose().insert(pose)

print("Database test successful!")