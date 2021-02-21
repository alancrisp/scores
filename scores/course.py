from flask import (
    Blueprint, redirect, render_template, request, url_for
)

from . import db
from scores.form.courseform import CourseForm

bp = Blueprint('course', __name__, url_prefix='/course')

@bp.route('')
def courses():
    cursor = db.connection.cursor()
    cursor.execute('SELECT * FROM course')
    courses = cursor.fetchall()
    return render_template('courses.html', courses=courses)

@bp.route('/<course_id>')
def view(course_id=0):
    cursor = db.connection.cursor()
    cursor.execute(
        '''SELECT * FROM course WHERE courseId = %s''',
        (course_id)
    )
    course = cursor.fetchone()
    return render_template('course-view.html', course=course)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    form = CourseForm(request.form)
    if request.method == 'POST' and form.validate():
        cursor = db.connection.cursor()
        cursor.execute(
            '''INSERT INTO course (name, location, city, holes) VALUES (%s, %s, %s, %s)''',
            (form.name.data, form.location.data, form.city.data, form.holes.data)
        )
        db.connection.commit()
        return redirect(url_for('course.view', course_id=cursor.lastrowid))

    return render_template('course-create.html', form=form)
