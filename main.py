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