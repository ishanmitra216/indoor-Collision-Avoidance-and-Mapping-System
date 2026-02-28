from fastapi import APIRouter
from controllers.robot_controller import get_robot_state

router = APIRouter(prefix="/robot", tags=["Robot"])

@router.get("/state")
def robot_state():
    return get_robot_state()