# main.py

from fastapi import FastAPI
from routes import pose, map, collision, robot

app = FastAPI(title="JetBot Navigation API")

app.include_router(pose.router)
app.include_router(map.router)
app.include_router(collision.router)
app.include_router(robot.router)

@app.get("/")
def root():
    return {"message": "JetBot Indoor Navigation API Running"}