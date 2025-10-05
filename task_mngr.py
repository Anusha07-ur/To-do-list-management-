from task import Task
from file_handler import load_tasks, save_tasks

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, title, description="", due_date=None):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, title, description, due_date)
        self.tasks.append(new_task)
        save_tasks(self.tasks)

    def list_tasks(self):
        return self.tasks

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        save_tasks(self.tasks)

    def update_task_status(self, task_id, status):
        for task in self.tasks:
            if task.task_id == task_id:
                task.status = status
        save_tasks(self.tasks)
