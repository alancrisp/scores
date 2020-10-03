from flask import (
    Blueprint, render_template, request, url_for
)

from scores.form.courseform import CourseForm

bp = Blueprint('course', __name__, url_prefix='/course')

@bp.route('')
def courses():
    return render_template('courses.html')

@bp.route('/create', methods=('GET', 'POST'))
def create():
    form = CourseForm(request.form)
    if request.method == 'POST' and form.validate():
        return 'TODO: create course' # TODO

    return render_template('course-create.html')
