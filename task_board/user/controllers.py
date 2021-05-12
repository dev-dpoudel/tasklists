from flask import request, url_for
from flask_classful import FlaskView, route
from .models import User
from .serializers import user_schema, user_schemas
from task_board import db


class UserView(FlaskView):
    ''' Provides API Endpoint for User Models '''
    # : Route Prefix for Views
    route_prefix = '/user/'

    def index(self):
        ''' Base Endpoint for User '''
        users = User.query.all()
        return user_schemas.jsonify(users)

    def resource(self):
        '''Resource Endpoint for User '''
        return {"url": url_for("UserView:delete", pk=1)}

    def get(self, id):
        ''' Get Selected User '''
        user = User.query.get(id)
        return user_schema.jsonify(user)

    @route("/create/", methods=["POST"])
    def post(self):
        ''' Create a User instance '''
        data = user_schema.load(request.json['users'])
        post = User(**data)
        db.session.add(post)
        db.session.commit()
        result = user_schema.dump(post)
        return {"data": result}

    @route("/<int:pk>/", methods=["PUT"])
    def put(self, pk):
        ''' Update a User Instance '''
        data = user_schema.load(request.json['users'])
        User.query.filter_by(id=pk).update(data)
        db.session.commit()
        return {"success": True}

    @route("/<int:pk>/", methods=["PATCH"])
    def patch(self, pk):
        ''' Patch a User Instance '''
        data = user_schema.load(request.json['users'], partial=True)
        User.query.filter_by(id=pk).update(data)
        db.session.commit()
        return {"success": True}

    @route("/<int:pk>", methods=["DELETE"])
    def delete(self, pk):
        ''' Delete a User Instance '''
        result = User.query.filter_by(id=pk).delete()
        db.session.commit()
        return {"success": result}
