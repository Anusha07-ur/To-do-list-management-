import json
import os
from task import Task

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return [Task.from_dict(task) for task in data]

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)
