from fastapi import APIRouter
from controllers.pose_controller import get_latest_pose

router = APIRouter(prefix="/pose", tags=["Pose"])

@router.get("/latest")
def latest_pose():
    return get_latest_pose()