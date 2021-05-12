from flask import url_for, request
from flask_classful import FlaskView, route
from .models import Task
from .serializers import TaskSerializers
from task_board import db
from task_board.viewMixin import BaseVeiwMixin


class TaskView(FlaskView, BaseVeiwMixin):
    ''' Provides API Endpoint for Task Models '''
    # : Route Prefix for Views
    route_prefix = '/task/'
    Model = Task
    Serializer = TaskSerializers
    session = db.session

    def index(self):
        ''' Base Endpoint for Task '''
        return self._index()

    def get(self, pk):
        ''' Base Endpoint for Task '''
        return self._get(pk)

    def resource(self):
        '''Resource Endpoint for Task '''
        return {"url": url_for("TaskView:post")}

    @route("/", methods=["POST"])
    def post(self):
        ''' Create a Task instance '''
        data = request.args["task"]
        return self._post(input_data=data)

    @route("/", methods=["PUT"])
    def put(self):
        ''' Update a Task Instance '''
        data = request.args["task"]
        return self._put(input_data=data)

    @route("/<int:pk>", methods=["PATCH"])
    def patch(self, pk):
        ''' Patch a Task Instance '''
        data = request.args["task"]
        return self._patch(pk=pk, input_data=data)

    @route("/<int:pk>", methods=["DELETE"])
    def delete(self, pk):
        ''' Delete a Task Instance '''
        return self._delete(pk)
