from task_board import marshmallow
from .models import Task
from marshmallow import fields


class TaskSerializers(marshmallow.SQLAlchemyAutoSchema):
    ''' Serializer class for Tasks '''

    # created_at is "read-only"
    created_at = fields.DateTime(dump_only=True)

    class Meta:
        ''' Meta Definition for TaskSerializers '''
        model = Task
        include_fk = True
