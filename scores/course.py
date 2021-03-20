from flask import (
    Blueprint, redirect, render_template, request, url_for
)
from injector import inject

from scores.form.courseform import CourseForm
from scores.repo.courserepo import CourseRepo

bp = Blueprint('course', __name__, url_prefix='/course')

@inject
@bp.route('')
def courses(repo: CourseRepo):
    courses = repo.get_all()
    return render_template('courses.html', courses=courses)

@inject
@bp.route('/<course_id>')
def view(repo: CourseRepo, course_id=0):
    course = repo.get_by_id(course_id)
    return render_template('course-view.html', course=course)

@inject
@bp.route('/create', methods=('GET', 'POST'))
def create(repo: CourseRepo):
    form = CourseForm(request.form)
    if request.method == 'POST' and form.validate():
        course_id = repo.create(form.name.data, form.location.data, form.city.data, form.holes.data)
        return redirect(url_for('course.view', course_id=course_id))

    return render_template('course-create.html', form=form)
