from flask_classful import FlaskView
from .models import User
from .serializers import user_schema


class UserView(FlaskView):
    ''' Provides API Endpoint for User Models '''
    # : Route Prefix for Views
    route_prefix = '/user/'

    def index(self):
        ''' Base Endpoint for User '''
        users = User.query.all()
        return user_schema.jsonify(users), 200
