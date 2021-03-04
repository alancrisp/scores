from flask import (
    Blueprint, redirect, render_template, request, url_for
)

from . import db
from scores.form.eventform import EventForm
from scores.repo.eventrepo import EventRepo
from scores.repo.courserepo import CourseRepo

bp = Blueprint('event', __name__, url_prefix='/event')

@bp.route('')
def events():
    repo = EventRepo(db.connection)
    events = repo.get_all()
    return render_template('events.html', events=events)

@bp.route('/<event_id>')
def view(event_id=0):
    repo = EventRepo(db.connection)
    event = repo.get_by_id(event_id)
    return render_template('event-view.html', event=event)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    form = EventForm(request.form)
    if request.method == 'POST' and form.validate():
        repo = EventRepo(db.connection)
        repo.create(form.course.data, form.date.data)
        return redirect(url_for('event.events')) #TODO redirect to event

    courserepo = CourseRepo(db.connection)
    form.course.choices = [(c['courseId'], c['name']) for c in courserepo.get_menu_options()]

    return render_template('event-create.html', form=form)
