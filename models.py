# Каждая задача должна содержать заголовок и описание.
# Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).

from typing import Optional
from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    title: str
    body: str = None
    status: bool = False
    is_active: bool = True

class New_Task(BaseModel):
    title: str
    body: str = None
    status: bool = False
    is_active: bool = True
