from fastapi import APIRouter, HTTPException, Query
from src.tasks.schemas import *
from src.tasks.core import TaskCore
from typing import Annotated, List

router = APIRouter()

@router.get("/")
async def get_tasks(params: Annotated[GetTasksParams, Query()]) -> List[TaskModel]:
    order_by, order_type, limit = (
        params.order_by, params.order_type, params.limit
    )
    tasks = await TaskCore.find_all(
        order_by=order_by,
        order_type=order_type,
        limit=limit
    )

    response = [TaskModel(**i.__dict__) for i in tasks]
    return response

@router.get("/{task_id}")
async def get_task(task_id: int) -> TaskModel:
    task = await TaskCore.find_one(id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/")
async def create_task(task: TaskInput) -> int:
    print(task)
    task_id = await TaskCore.add(**task.__dict__)
    return task_id

@router.put("/{task_id}")
async def update_task(task_id: int, task: TaskInput) -> TaskModel:
    update = await TaskCore.update({"id": task_id}, **task.__dict__)
    if not update:
        raise HTTPException(status_code=404, detail="Task not found")
    updated_task = await TaskCore.find_one(id=task_id)
    response = TaskModel(**updated_task.__dict__)
    return response

@router.delete("/{task_id}")
async def delete_task(task_id: int) -> None:
    result = await TaskCore.delete(id=task_id)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
