from flask import url_for, request
from flask_classful import FlaskView, route
from .models import Task
from .serializers import task_schema, task_schemas
from task_board import db


class TaskView(FlaskView):
    ''' Provides API Endpoint for Task Models '''
    # : Route Prefix for Views
    route_prefix = '/task/'

    def get(self, id):
        ''' Base Endpoint for Task '''
        tasks = Task.query.filter_by(id=id)
        return task_schemas.jsonify(tasks)

    def resource(self):
        '''Resource Endpoint for Task '''
        return {"url": url_for("TaskView:post")}
        tasks = Task.query.all()
        return task_schemas.jsonify(tasks)

    @route("/create/", methods=["post"])
    def post(self):
        ''' Create a Task instance '''
        data = task_schema.load(request.json['tasks'], partial=True)
        post = Task(**data)
        db.session.add(post)
        db.session.commit()
        result = task_schema.dump(post)
        return {"data": result}

    @route("/update/", methods=["put"])
    def update(self):
        ''' Update a Task Instance '''
        return {"success": True}

    @route("/update/", methods=["patch"])
    def patch(self):
        ''' Patch a Task Instance '''
        return {"success": True}

    @route("/delete/<int:pk>", methods=["delete"])
    def delete(self, pk):
        ''' Delete a Task Instance '''
        Task.query.filter(id=pk).delete()
        db.session.commit()
        return {"success": True}
