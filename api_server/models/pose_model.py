from pydantic import BaseModel

class PoseResponse(BaseModel):
    x: float
    y: float
    theta: float
    timestamp: str