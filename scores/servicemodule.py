from injector import Module
from flask_mysqldb import MySQL

from scores.repo.courserepo import CourseRepo
from scores.repo.eventrepo import EventRepo
from scores.repo.playerrepo import PlayerRepo
from scores.repo.scorerepo import ScoreRepo

class ServiceModule(Module):
    def __init__(self, app):
        self.app = app

    def configure(self, binder):
        db = self.create_db()
        binder.bind(CourseRepo, to=CourseRepo(db))
        binder.bind(EventRepo, to=EventRepo(db))
        binder.bind(PlayerRepo, to=PlayerRepo(db))
        binder.bind(ScoreRepo, to=ScoreRepo(db))

    def create_db(self):
        db = MySQL()
        db.init_app(self.app)
        return db
