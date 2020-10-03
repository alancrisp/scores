from flask import (
    Blueprint, render_template, request, url_for
)

bp = Blueprint('course', __name__, url_prefix='/course')

@bp.route('')
def courses():
    return render_template('courses.html')
