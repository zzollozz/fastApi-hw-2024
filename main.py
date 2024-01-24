from fastapi import FastAPI

from typing import List

from models import Task, New_Task
from data_db import database, task_table

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def root():
    return {"List_Tasks": '/tasks'}

@app.get("/tasks", response_model=List[Task])
async def read_tasks():
    query = task_table.select()
    return await database.fetch_all(query)


@app.get("/task/{task_id}", response_model=Task)
async def get_task(task_id: int):
    item_task = task_table.select().where(task_table.c.id == task_id)
    return await database.fetch_one(item_task)


@app.post("/tasks/", response_model=Task)
async def create_task(new_task: New_Task):
    query = task_table.insert().values(
        title=new_task.title,
        body=new_task.body,
        status=new_task.status,
        is_active=new_task.is_active
    )
    last_record_id = await database.execute(query)
    return await database.fetch_all(query)


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, new_task: New_Task):
    item_task = task_table.update().where(task_table.c.id == task_id).values(
        title=new_task.title,
        body=new_task.body,
        status=new_task.status,
        is_active=new_task.is_active
    )
    await database.execute(item_task)
    return {**new_task.dict(), "id": task_id}


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    item_task = task_table.delete().where(task_table.c.id == task_id)
    await database.execute(item_task)
    return {'message': 'Task deleted'}
