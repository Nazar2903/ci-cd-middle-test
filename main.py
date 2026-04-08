import json
import os
import uuid

class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump([], f)

    def _load_tasks(self):
        with open(self.filename, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def _save_tasks(self, tasks):
        with open(self.filename, 'w') as f:
            json.dump(tasks, f, indent=4)
            
    def add_task(self, description, date, priority):
        tasks = self._load_tasks()
        task_id = str(uuid.uuid4())[:8]
        task = {
            "id": task_id,
            "description": description,
            "date": date,
            "priority": priority
        }
        tasks.append(task)
        self._save_tasks(tasks)
        return task_id
    
    def delete_task(self, task_id):
        tasks = self._load_tasks()
        tasks = [t for t in tasks if t["id"] != task_id]
        self._save_tasks(tasks)
        
    def list_tasks(self, sort_by="priority"):
        tasks = self._load_tasks()
        if sort_by == "priority":
            tasks.sort(key=lambda x: x["priority"])
        elif sort_by == "date":
            tasks.sort(key=lambda x: x["date"])
        return tasks