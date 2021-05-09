from task_board import db


class Task(db.Model):
    ''' User Class Definition '''
    # : Table Name in database
    __tablename__ = 'tasks'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    user = db.Column(
        db.Integer,
        db.ForeignKey('person.id', nullable=False)
    )
    priority = db.Column(
        db.String(16),
        nullable=False
    )
    subtasks = db.Column(
        db.String(120),
        nullable=False
    )
    title = db.Column(
        db.String(250),
        nullable=False
    )
    description = db.Column(
        db.String(1000),
        nullable=False
    )

    def __repr__(self):
        return '<Task {0}>'.format(self.title)
