from task_board import marshmallow
from .models import User


class UserSerializers(marshmallow.SQLAlchemyAutoSchema):
    ''' Serializer class for Tasks '''

    # password is "write-only"
    password = marshmallow.fields.Str(load_only=True)
    # created_at is "read-only"
    created_at = marshmallow.fields.DateTime(dump_only=True)

    class Meta:
        ''' Meta Definition for TaskSerializers '''
        model = User
        include_fk = True
