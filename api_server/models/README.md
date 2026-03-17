# Models Directory

This folder contains Pydantic schemas used by the API server to define
response shapes for map and pose data.

## Purpose

- Keep API payload structure explicit and documented.
- Enable optional FastAPI response validation and OpenAPI schema generation.
- Provide reusable typed models for route and controller responses.

## Files

### pose_model.py

Defines `PoseResponse`, a Pydantic model for robot pose output.

Fields:
- `x: float` - Robot x-coordinate in map/world frame.
- `y: float` - Robot y-coordinate in map/world frame.
- `theta: float` - Robot heading/orientation.
- `timestamp: str` - Time when the pose was recorded.

Typical payload:

```json
{
	"x": 1.24,
	"y": -0.55,
	"theta": 0.78,
	"timestamp": "2026-03-17 10:15:00"
}
```

### map_model.py

Defines `MapResponse`, a Pydantic model for occupancy map output.

Fields:
- `width: int` - Map width in cells/pixels.
- `height: int` - Map height in cells/pixels.
- `map_data_base64: str` - Base64-encoded binary map data for JSON transport.

Typical payload:

```json
{
	"width": 400,
	"height": 400,
	"map_data_base64": "AAECAwQF..."
}
```

## How These Models Are Used

Current controllers in the API server return dictionaries directly. These
models are still useful as canonical schemas and can be attached to route
decorators using `response_model`.

Example:

```python
from fastapi import APIRouter
from models.pose_model import PoseResponse

router = APIRouter(prefix="/pose", tags=["Pose"])

@router.get("/latest", response_model=PoseResponse)
def latest_pose():
		...
```

## Notes

- Keep field names aligned with controller response keys.
- If database timestamp format changes, update `timestamp` typing or parsing.
- If map encoding changes (for example compressed bytes), update
	`map_data_base64` description and related controller logic.
