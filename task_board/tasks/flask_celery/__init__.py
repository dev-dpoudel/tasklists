from flask import Flask
from flask_cors import CORS
from .controllers import AppView
from celery import Celery


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL'],
        include=app.config['CELERY_TASKS']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')
CORS(app)
AppView.register(app)
celery = make_celery(app)  # noqa
