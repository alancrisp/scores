from injector import Module
from flask_mysqldb import MySQL

from scores.repo.courserepo import CourseRepo
from scores.repo.eventrepo import EventRepo

class ServiceModule(Module):
    def __init__(self, app):
        self.app = app

    def configure(self, binder):
        db = self.create_db()
        binder.bind(CourseRepo, to=CourseRepo(db))
        binder.bind(EventRepo, to=EventRepo(db))

    def create_db(self):
        db = MySQL()
        db.init_app(self.app)
        return db
