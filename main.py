from fastapi import FastAPI, HTTPException
from models import Task
from database import read_tasks, save_tasks

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to the Task Manager API"}

@app.get("/tasks")
def get_tasks():
    return read_tasks()

@app.post("/tasks")
def create_task(task: Task):
    tasks = read_tasks()
    tasks.append(task.dict())
    save_tasks(tasks)
    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    tasks = read_tasks()
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks[i] = updated_task.dict()
            save_tasks(tasks)
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = read_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    save_tasks(new_tasks)
    return {"message": "Task deleted"}
