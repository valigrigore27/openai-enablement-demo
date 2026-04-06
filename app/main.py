from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI(title="OpenAI Enablement Demo API")


class TaskCreate(BaseModel):
    title: str
    done: bool = False


class Task(TaskCreate):
    id: int


tasks_db: List[Task] = [
    Task(id=1, title="Prepare GitHub demo", done=False),
    Task(id=2, title="Create first issue", done=False),
]


@app.get("/")
def read_root():
    return {"message": "FastAPI demo is running"}


@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks_db


@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    new_task = Task(id=len(tasks_db) + 1, title=task.title, done=task.done)
    tasks_db.append(new_task)
    return new_task
