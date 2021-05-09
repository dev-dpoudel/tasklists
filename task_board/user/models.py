from task_board import db


class User(db.Model):
    ''' User Class Definition '''
    # : Table Name in Database
    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    first_name = db.Column(
        db.String(32),
        nullable=False
    )
    last_name = db.Column(
        db.String(32)
    )
    role = db.Column(
        db.String(16)
    )
    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )
    tasks = db.relationship('Task', backref='users', lazy=True)

    def __repr__(self):
        return '<User {0} {1}>'.format(self.first_name, self.last_name)
