from .api import get, post, put, delete

def fetch_tasks():
    return get("/tasks")

def create_task(task_data):
    post("/tasks", task_data)

def update_task(task_id, task_data):
    put(f"/tasks/{task_id}", task_data)

def delete_task(task_id):
    delete(f"/tasks/{task_id}")
