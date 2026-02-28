from services.db_service import DBService

db = DBService()

def get_latest_pose():

    pose = db.get_latest_pose()

    if pose:
        return {
            "x": pose[0],
            "y": pose[1],
            "theta": pose[2],
            "timestamp": pose[3]
        }

    return {"message": "No pose data available"}