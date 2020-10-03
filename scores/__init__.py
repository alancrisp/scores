import os

from flask import Flask
from flask import render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import course
    app.register_blueprint(course.bp)

    @app.route('/')
    def home():
        return events()

    @app.route('/events')
    def events():
        return render_template('events.html')

    return app
