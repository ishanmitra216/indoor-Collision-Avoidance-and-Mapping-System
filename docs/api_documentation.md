# API Documentation

Base URL:
http://localhost:8000

---

## GET /pose/latest

Returns latest robot pose.

Response:
{
  "x": 1.23,
  "y": 0.45,
  "theta": 0.0,
  "timestamp": "2026-02-28"
}

---

## GET /map/latest

Returns latest occupancy grid map (Base64 encoded).

---

## GET /collision/status

Returns collision detection status.

---

## GET /robot/state

Returns robot state information.