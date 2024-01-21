# Каждая задача должна содержать заголовок и описание.
# Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).

from typing import Optional
from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    body: Optional[str] = None
    status: Optional[bool] = False
    is_active: Optional[bool] = True
