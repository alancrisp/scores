from flask import (
    Blueprint, redirect, render_template, request, url_for
)

from . import db
from scores.form.eventform import EventForm

bp = Blueprint('event', __name__, url_prefix='/event')

@bp.route('')
def events():
    cursor = db.connection.cursor()
    cursor.execute('SELECT e.*, c.name FROM event e INNER JOIN course c USING (courseId)')
    events = cursor.fetchall()
    return render_template('events.html', events=events)

@bp.route('/<event_id>')
def view(event_id=0):
    cursor = db.connection.cursor()
    cursor.execute(
        '''SELECT e.*, c.name, c.holes FROM event e INNER JOIN course c USING (courseId) WHERE eventId = %s''',
        (event_id)
    )
    event = cursor.fetchone()
    return render_template('event-view.html', event=event)

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
