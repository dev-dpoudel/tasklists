from task_board import marshmallow
from .models import User
from marshmallow import fields


class UserSerializers(marshmallow.SQLAlchemyAutoSchema):
    ''' Serializer class for User '''

    # password is "write-only"
    password = fields.Str(load_only=True)
    # created_at is "read-only"
    created_at = fields.DateTime(dump_only=True)
    # Nested Model Serialization
    tasks = marshmallow.Nested("TaskSerializers", many=True)

    class Meta:
        ''' Meta Definition for UserSerializers '''
        model = User
        include_fk = True


# Schema for single get
user_schema = UserSerializers()
# Schema for Lists
user_schemas = UserSerializers(many=True)
