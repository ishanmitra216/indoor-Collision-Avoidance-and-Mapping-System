from fastapi import APIRouter
from controllers.map_controller import get_latest_map

router = APIRouter(prefix="/map", tags=["Map"])

@router.get("/latest")
def latest_map():
    return get_latest_map()