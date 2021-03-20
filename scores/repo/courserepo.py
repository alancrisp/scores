from injector import inject
from flask_mysqldb import MySQL

class CourseRepo:
    def __init__(self, db: MySQL):
        self.db = db

    def get_all(self):
        cursor = self.db.connection.cursor()
        cursor.execute('SELECT * FROM course')
        return cursor.fetchall()

    def get_by_id(self, course_id):
        cursor = self.db.connection.cursor()
        cursor.execute(
            '''SELECT * FROM course WHERE courseId = %s''',
            (course_id,)
        )
        return cursor.fetchone()

    def get_menu_options(self):
        cursor = self.db.connection.cursor()
        cursor.execute('SELECT courseId, name FROM course ORDER BY name ASC')
        return cursor.fetchall()

    def create(self, name, location, city, holes):
        cursor = self.db.connection.cursor()
        cursor.execute(
            '''INSERT INTO course (name, location, city, holes) VALUES (%s, %s, %s, %s)''',
            (name, location, city, holes)
        )
        self.db.connection.commit()
        return cursor.lastrowid
