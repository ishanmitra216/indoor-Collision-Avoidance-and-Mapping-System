from fastapi import APIRouter
from controllers.robot_controller import get_collision_status

router = APIRouter(prefix="/collision", tags=["Collision"])

@router.get("/status")
def collision_status():
    return get_collision_status()