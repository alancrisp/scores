from flask import (
    Blueprint, redirect, render_template, request, url_for
)

from . import db
from scores.form.eventform import EventForm

bp = Blueprint('event', __name__, url_prefix='/event')

@bp.route('')
def events():
    return render_template('events.html')

@bp.route('/create', methods=('GET', 'POST'))
def create():
    cursor = db.connection.cursor()

    form = EventForm(request.form)
    if request.method == 'POST' and form.validate():
        cursor.execute(
            '''INSERT INTO event (courseId, eventDate) VALUES (%s, %s)''',
            (form.course.data, form.date.data)
        )
        db.connection.commit()
        return redirect(url_for('event.events')) #TODO redirect to event

    cursor.execute('SELECT courseId, name FROM course ORDER BY name ASC')
    courses = cursor.fetchall()
    form.course.choices = [(c['courseId'], c['name']) for c in courses]

    return render_template('event-create.html', form=form)
