
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        task = {
            "id": self.next_id,
            "title": title,
            "completed": False
        }

        self.tasks.append(task)
        self.next_id += 1

        return task

    def display_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return True

        return False

    def delete_task(self, task_id):
        if not isinstance(task_id, int) or isinstance(task_id, bool):
            return False

        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return True

        return False
