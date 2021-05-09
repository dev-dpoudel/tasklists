from flask_classful import FlaskView
from .models import Task
from .serializers import TaskSerializers


class TaskView(FlaskView):
    ''' Provides API Endpoint for User Models '''
    # : Route Prefix for Views
    route_prefix = '/task/'

    def index(self):
        ''' Base Endpoint for User '''
        tasks = Task.query.all()
        return TaskSerializers(**tasks)
