from pydantic import BaseModel

class MapResponse(BaseModel):
    width: int
    height: int
    map_data_base64: str