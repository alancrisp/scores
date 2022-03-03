import os

from flask import Flask
from flask import render_template

from injector import Injector, inject
from flask_injector import FlaskInjector

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    app.config['MYSQL_HOST'] = os.environ.get('DB_HOST')
    app.config['MYSQL_USER'] = os.environ.get('DB_USER')
    app.config['MYSQL_PASSWORD'] = os.environ.get('DB_PASSWORD')
    app.config['MYSQL_DB'] = os.environ.get('DB_DATABASE')
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import course
    from . import event
    from . import player
    from . import stats
    app.register_blueprint(course.bp)
    app.register_blueprint(event.bp)
    app.register_blueprint(player.bp)
    app.register_blueprint(stats.bp)

    from scores.repo.eventrepo import EventRepo

    @inject
    @app.route('/')
    def home(repo: EventRepo):
        return event.events(repo)

    from .servicemodule import ServiceModule
    injector = Injector([ServiceModule(app)])
    FlaskInjector(app=app, injector=injector)

    return app
