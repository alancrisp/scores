import os

from flask import Flask
from flask import render_template
from flask_mysqldb import MySQL

db = MySQL()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    app.config['MYSQL_HOST'] = os.environ.get('DB_HOST')
    app.config['MYSQL_USER'] = os.environ.get('DB_USER')
    app.config['MYSQL_PASSWORD'] = os.environ.get('DB_PASSWORD')
    app.config['MYSQL_DB'] = os.environ.get('DB_DATABASE')

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    from . import course
    from . import event
    app.register_blueprint(course.bp)
    app.register_blueprint(event.bp)

    @app.route('/')
    def home():
        return event.events()

    return app
