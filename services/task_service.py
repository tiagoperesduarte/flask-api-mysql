from models.task import Task


class TaskService:
    def get_tasks(self):
        return Task.query.all()

    def get_task_by_id(self, id):
        return Task.query.get(id)

    def save_task(self, task):
        return task.save()

    def delete_task_by_id(self, id):
        task = self.get_task_by_id(id)

        if task:
            task.delete()
