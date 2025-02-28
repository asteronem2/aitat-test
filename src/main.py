from fastapi import FastAPI
from src.tasks.router import router as tasks_router

app = FastAPI()

app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])
