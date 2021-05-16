from flask import (
    Blueprint, redirect, render_template, request, url_for
)
from injector import inject

from scores.form.playerform import PlayerForm
from scores.repo.playerrepo import PlayerRepo

bp = Blueprint('player', __name__, url_prefix='/player')

@inject
@bp.route('')
def players(repo: PlayerRepo):
    players = repo.get_all()
    return render_template('players.html', players=players)

@inject
@bp.route('/<player_id>')
def view(repo: PlayerRepo, player_id=0):
    player = repo.get_by_id(player_id)
    return render_template('player-view.html', player=player)

@inject
@bp.route('/create', methods=('GET', 'POST'))
def create(repo: PlayerRepo):
    form = PlayerForm(request.form)
    if request.method == 'POST' and form.validate():
        player_id = repo.create(form.name.data)
        return redirect(url_for('player.view', player_id=player_id))

    return render_template('player-create.html', form=form)
