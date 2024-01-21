from fastapi import FastAPI

from models import Task
from config import test_task

app = FastAPI()


@app.get("/")
@app.get("/task")
async def root():
    return {"Tasks": test_task}


@app.get("/task/{id}")
async def get_task(id: int):
    for task in test_task:
        if task['id'] == id:
            return {f"Task {id}": task}
    return {"Task": 'NotFound'}


@app.post("/tasks/")
async def create_task(task: Task):
    print(f"{task=}")
    test_task.append(dict(task))
    return {f"Task": task}


@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    for t in test_task:
        if t['id'] == task_id:
            t.update(task)
            return {'task_id': task_id, 'task': t}
    return {"Task": 'NotFound'}


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, task: Task):
    for t in test_task:
        if t['id'] == task_id:
            t.update(is_active=False)
            return {f'DELETE Task: {t}'}
    return {"Task": 'NotFound'}
