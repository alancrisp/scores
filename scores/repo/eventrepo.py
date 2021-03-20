from injector import inject
from flask_mysqldb import MySQL

class EventRepo:
    def __init__(self, db: MySQL):
        self.db = db

    def get_all(self):
        cursor = self.db.connection.cursor()
        cursor.execute('SELECT e.*, c.name FROM event e INNER JOIN course c USING (courseId)')
        return cursor.fetchall()

    def get_by_id(self, event_id):
        cursor = self.db.connection.cursor()
        cursor.execute(
            '''SELECT e.*, c.name, c.holes FROM event e INNER JOIN course c USING (courseId) WHERE eventId = %s''',
            (event_id,)
        )
        return cursor.fetchone()

    def create(self, course_id, event_date):
        cursor = self.db.connection.cursor()
        cursor.execute(
            '''INSERT INTO event (courseId, eventDate) VALUES (%s, %s)''',
            (course_id, event_date,)
        )
        self.db.connection.commit()
