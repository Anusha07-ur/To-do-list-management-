import datetime

class Task:
    def __init__(self, task_id, title, description="", due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date if due_date else str(datetime.date.today())
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["task_id"],
            data["title"],
            data.get("description", ""),
            data.get("due_date"),
            data.get("status", "Pending")
        )
