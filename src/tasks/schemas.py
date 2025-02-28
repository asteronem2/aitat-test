from datetime import datetime

from pydantic import BaseModel
from pydantic.fields import Field
from typing_extensions import Literal

class TaskModel(BaseModel):
    id: int
    title: str = Field(max_length=255)
    description: str|None = Field(max_length=1024)
    created_at: datetime
    updated_at: datetime

class GetTasksParams(BaseModel):
    order_by: str = "id"
    order_type: Literal["asc", "desc"] = "asc"
    limit: int|None = None

class TaskInput(BaseModel):
    title: str = Field(max_length=255)
    description: str|None = Field(max_length=1024)

