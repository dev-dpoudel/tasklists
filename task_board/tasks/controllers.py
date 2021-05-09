from flask_classful import FlaskView
from .models import User
from .serialzers import TaskSerializers


class TaskView(FlaskView):
    ''' Provides API Endpoint for User Models '''
    # : Route Prefix for Views
    route_prefix = '/user/'

    def index(self):
        ''' Base Endpoint for User '''
        users = User.object.get.all()
        return TaskSerializers(**users)
