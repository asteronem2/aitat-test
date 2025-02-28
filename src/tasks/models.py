from datetime import datetime
from typing import Annotated

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, DateTime, func

from src.database import Base

created_at = Annotated[datetime, mapped_column(DateTime(timezone=True), server_default=func.now())]
updated_at = Annotated[datetime, mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())]

class Task(Base):
    id = mapped_column(Integer, primary_key=True)
    title: Mapped[str|None] = mapped_column(String(255))
    description: Mapped[str|None] = mapped_column(String(1024))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
