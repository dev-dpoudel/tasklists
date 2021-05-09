from flask_classful import FlaskView
from .models import Task
from .serializers import task_schema


class TaskView(FlaskView):
    ''' Provides API Endpoint for User Models '''
    # : Route Prefix for Views
    route_prefix = '/task/'

    def index(self):
        ''' Base Endpoint for User '''
        tasks = Task.query.all()
        return task_schema.jsonify(tasks)
