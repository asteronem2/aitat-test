from src.database import BaseCore
from src.tasks.models import Task


class TaskCore(BaseCore):
    model = Task