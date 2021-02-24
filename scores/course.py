from flask import (
    Blueprint, redirect, render_template, request, url_for
)

from . import db
from scores.form.courseform import CourseForm
from scores.repo.courserepo import CourseRepo

bp = Blueprint('course', __name__, url_prefix='/course')

@bp.route('')
def courses():
    repo = CourseRepo(db.connection)
    courses = repo.get_all()
    return render_template('courses.html', courses=courses)

@bp.route('/<course_id>')
def view(course_id=0):
    repo = CourseRepo(db.connection)
    course = repo.get_by_id(course_id)
    return render_template('course-view.html', course=course)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    form = CourseForm(request.form)
    if request.method == 'POST' and form.validate():
        repo = CourseRepo(db.connection)
        course_id = repo.create(form.name.data, form.location.data, form.city.data, form.holes.data)
        return redirect(url_for('course.view', course_id=course_id))

    return render_template('course-create.html', form=form)
