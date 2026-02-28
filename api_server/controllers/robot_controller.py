from services.robot_service import RobotService

robot_service = RobotService()

def get_robot_state():
    return robot_service.get_state()

def get_collision_status():
    return robot_service.get_collision_status()