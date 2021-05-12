from flask import request


class BaseProperties:
    """
    Provides base configuration for view Models.

    Args:
        Model (db.Model): Base Model to operate on
        Serializer (sqlalchemy.schema): Base Model to operate on
        Filters (dictionary): Filter Parameters
        Order (list): Ordering
        limit (int) : Item Count for Pagination
        skip (int)  : Recods to jump to

    Raises:
        Exception: description

    """
    Model = None
    Serializer = None
    Filters = None
    Order = None
    limit = 10
    skip = 0
    session = None


class BaseVeiwMixin(BaseProperties):
    """
    Provides base service and configuration for view Models.

    Args:
        Model (db.Model): Base Model to operate on
        Entity (sqlalchemy.schema): Base Model to operate on
        Filters (dictionary): Filter Parameters
        Ordering (list): Ordering
        limit (int) : Item Count for Pagination
        skip (int)  : Recods to jump to

    Raises:
        Exception: EntityNotFoundError
        Exception: MultipleEntityFoundError
        Exceptions: OperationError
        Exceptions: IntegrityError

    """

    def __init__(self):
        self._schema = self.Serializer()
        self._schemas = self.Serializer(many=True)

    def _queryset(self):
        ''' Initialize Base class '''
        self._schema = self.Serializer()
        self._schemas = self.Serializer(many=True)

    def _index(self):
        ''' Base Endpoint for Listing Model '''
        instances = self.Model.query.all()
        return self._schemas.jsonify(instances)

    def _get(self, pk):
        ''' Get Selected Model '''
        instance = self.Model.get(id=pk)
        return self._schema.jsonify(instance)

    def _list(self, filters):
        ''' Base Endpoint for Listing Model '''
        instances = self.Model.query.filter_by(**filters)
        return self._schemas.jsonify(instances)

    def _post(self):
        ''' Create a Model instance '''
        data = self._schema.load(request.json['data'])
        instance = self.Model(**data)
        self.session.add(instance)
        self.session.commit()
        return self._schema.jsonify(instance)

    def _put(self, pk):
        ''' Update a Model Instance '''
        instance = self._schema.load(request.json['data'])
        self.Model.query.filter_by(id=pk).update(instance)
        self.session.commit()
        return self._schema.jsonify(instance)

    def _patch(self, pk):
        ''' Patch a Model Instance '''
        instance = self._schema.load(request.json['data'], partial=True)
        self.Model.query.filter_by(id=pk).update(instance)
        self.session.commit()
        return self._schema.jsonify(instance)

    def _delete(self, pk):
        ''' Delete a Model instance '''
        result = self.Model.query.filter_by(id=pk).delete()
        self.session.commit()
        return {"succes": result}


class MultiModelMixin:
    """
    Provides base service and configuration for Bulk actions.

    Args:
        Model (db.Model): Base Model to operate on
        Entity (sqlalchemy.schema): Base Model to operate on
        Filters (dictionary): Filter Parameters
        Ordering (list): Ordering
        limit (int) : Item Count for Pagination
        skip (int)  : Recods to jump to

    Raises:
        Exception: EntityNotFoundError
        Exception: MultipleEntityFoundError
        Exceptions: OperationError
        Exceptions: IntegrityError

    """

    def _post(self):
        ''' Create a Model instance '''
        data_list = self._schemas.load(request.json['data'])
        instances = [self.Model(**data) for data in data_list]
        self.session.bulk_save_objects(instances)
        self.session.commit()
        return self._schemas.jsonify(instances)

    def _patch(self, filter):
        ''' Patch a Model Instance '''
        instance = self._schema.load(request.json['data'], partial=True)
        self.Model.query.filter_by(**filter).update(instance)
        self.session.commit()
        return self._schema.jsonify(instance)

    def _delete(self, filter):
        ''' Delete a Model instance '''
        result = self.Model.query.filter_by(**filter).delete()
        self.session.commit()
        return {"succes": result}
