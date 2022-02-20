from flask import (
    Blueprint, redirect, render_template, request, url_for
)
from injector import inject

from scores.form.eventform import EventForm
from scores.form.eventplayerform import EventPlayerForm
from scores.repo.courserepo import CourseRepo
from scores.repo.eventrepo import EventRepo
from scores.repo.playerrepo import PlayerRepo

bp = Blueprint('event', __name__, url_prefix='/event')

@inject
@bp.route('')
def events(repo: EventRepo):
    events = repo.get_all()
    return render_template('events.html', events=events)

@inject
@bp.route('/<event_id>', methods=('GET', 'POST'))
def view(repo: EventRepo, playerrepo: PlayerRepo, event_id=0):
    event = repo.get_by_id(event_id)
    form = EventPlayerForm(request.form, eventId=event_id) # TODO add to service container
    form.player.choices = [(p['playerId'], p['name']) for p in playerrepo.get_menu_options_for_event(event_id)]
    if request.method == 'POST' and form.validate():
        return redirect(url_for('event.add_player', event_id=event_id, player_id=form.player.data))

    return render_template('event-view.html', event=event, form=form)

@inject
@bp.route('/create', methods=('GET', 'POST'))
def create(repo: EventRepo, courserepo: CourseRepo):
    form = EventForm(request.form) # TODO add to service container
    if request.method == 'POST' and form.validate():
        repo.create(form.course.data, form.date.data)
        return redirect(url_for('event.events')) #TODO redirect to event

    form.course.choices = [(c['courseId'], c['name']) for c in courserepo.get_menu_options()]

    return render_template('event-create.html', form=form)

@inject
@bp.route('/<event_id>/add-player/<player_id>', methods=('GET', 'POST'))
def add_player(repo: EventRepo, playerrepo: PlayerRepo, event_id=0, player_id=0):
    event = repo.get_by_id(event_id)
    player = playerrepo.get_by_id(player_id)
    return render_template('event-add-player.html', event=event, player=player)
