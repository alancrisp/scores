from flask import (
    Blueprint, redirect, render_template, request, url_for
)
from injector import inject

from scores.form.eventform import EventForm
from scores.repo.eventrepo import EventRepo
from scores.repo.courserepo import CourseRepo

bp = Blueprint('event', __name__, url_prefix='/event')

@inject
@bp.route('')
def events(repo: EventRepo):
    events = repo.get_all()
    return render_template('events.html', events=events)

@inject
@bp.route('/<event_id>')
def view(repo: EventRepo, event_id=0):
    event = repo.get_by_id(event_id)
    return render_template('event-view.html', event=event)

@inject
@bp.route('/create', methods=('GET', 'POST'))
def create(repo: EventRepo, courserepo: CourseRepo):
    form = EventForm(request.form) # TODO add to service container
    if request.method == 'POST' and form.validate():
        repo.create(form.course.data, form.date.data)
        return redirect(url_for('event.events')) #TODO redirect to event

    form.course.choices = [(c['courseId'], c['name']) for c in courserepo.get_menu_options()]

    return render_template('event-create.html', form=form)
