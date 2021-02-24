class CourseRepo:
    def __init__(self, connection):
        self.connection = connection

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM course')
        return cursor.fetchall()

    def get_by_id(self, course_id):
        cursor = self.connection.cursor()
        cursor.execute(
            '''SELECT * FROM course WHERE courseId = %s''',
            (course_id,)
        )
        return cursor.fetchone()

    def create(self, name, location, city, holes):
        cursor = self.connection.cursor()
        cursor.execute(
            '''INSERT INTO course (name, location, city, holes) VALUES (%s, %s, %s, %s)''',
            (name, location, city, holes)
        )
        self.connection.commit()
        return cursor.lastrowid
