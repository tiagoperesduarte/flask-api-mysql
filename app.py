from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)

    from resources.task_resource import TaskResource, TaskListResource

    api = Api(app)
    api.add_resource(TaskResource, '/tasks/<int:id>')
    api.add_resource(TaskListResource, '/tasks')

    return app
