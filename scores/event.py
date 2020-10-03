from flask import (
    Blueprint, render_template, request, url_for
)

bp = Blueprint('event', __name__, url_prefix='/event')

@bp.route('')
def events():
    return render_template('events.html')
