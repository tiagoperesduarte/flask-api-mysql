from flask_restful import Resource, reqparse

from models.task import Task
from services.task_service import TaskService

task_service = TaskService()

parser = reqparse.RequestParser()
parser.add_argument('description', type=str, required=True)
parser.add_argument('done', type=bool, required=True)


class TaskListResource(Resource):
    def get(self):
        return [task.to_dict() for task in task_service.get_tasks()]

    def post(self):
        data = parser.parse_args()
        saved_task = task_service.save_task(Task.from_dict(data))

        return saved_task.to_dict()


class TaskResource(Resource):
    def get(self, id):
        task = task_service.get_task_by_id(id)

        if not task:
            return {'message': 'Task not found'}, 404

        return task.to_dict()

    def put(self, id):
        task = task_service.get_task_by_id(id)

        if not task:
            return {'message': 'Task not found'}, 404

        data = parser.parse_args()
        task.description = data['description']
        task.done = data['done']

        saved_task = task_service.save_task(task)

        return saved_task.to_dict()

    def delete(self, id):
        task = task_service.get_task_by_id(id)

        if not task:
            return {'message': 'Task not found'}, 404

        task_service.delete_task_by_id(id)

        return {'message': 'Task deleted successfully'}
