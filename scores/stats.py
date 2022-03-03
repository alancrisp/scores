from flask import (
    Blueprint, render_template
)
from injector import inject

from scores.repo.scorerepo import ScoreRepo

bp = Blueprint('stats', __name__, url_prefix='/stats')

@inject
@bp.route('')
def stats(scorerepo: ScoreRepo):
    holes_in_one = scorerepo.get_holes_in_one_leaderboard()
    return render_template('stats.html', holes_in_one=holes_in_one);
