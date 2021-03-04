class EventRepo:
    def __init__(self, connection):
        self.connection = connection

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT e.*, c.name FROM event e INNER JOIN course c USING (courseId)')
        return cursor.fetchall()

    def get_by_id(self, event_id):
        cursor = self.connection.cursor()
        cursor.execute(
            '''SELECT e.*, c.name, c.holes FROM event e INNER JOIN course c USING (courseId) WHERE eventId = %s''',
            (event_id,)
        )
        return cursor.fetchone()

    def create(self, course_id, event_date):
        cursor = self.connection.cursor()
        cursor.execute(
            '''INSERT INTO event (courseId, eventDate) VALUES (%s, %s)''',
            (course_id, event_date,)
        )
        self.connection.commit()
