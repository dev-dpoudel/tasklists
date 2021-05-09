from flask import Flask
from flask_cors import CORS
from flask_celery import Celery
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


celery = Celery()
db = SQLAlchemy()
migrate = Migrate()
marshmallow = Marshmallow()


def create_app(mode_config=None):
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)

    if mode_config == "test":
        app.config.from_object('config.TestConfig')
    else:
        app.config.from_object('config.Config')

    CORS(app)
    celery.__init__(app)
    db.__init__(app)
    migrate.init_app(app, db)
    marshmallow.__init__(app)

    return app
