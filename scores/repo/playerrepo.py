from flask_mysqldb import MySQL

class PlayerRepo:
    def __init__(self, db: MySQL):
        self.db = db

    def get_all(self):
        cursor = self.db.connection.cursor()
        cursor.execute('SELECT * FROM player')
        return cursor.fetchall()

    def get_by_id(self, player_id):
        cursor = self.db.connection.cursor()
        cursor.execute(
            '''SELECT * FROM player WHERE playerId = %s''',
            (player_id,)
        )
        return cursor.fetchone()

    def get_menu_options_for_event(self, event_id):
        cursor = self.db.connection.cursor()
        cursor.execute(
            '''SELECT * FROM player p LEFT JOIN score s ON s.playerId = p.playerId AND s.eventId = %s WHERE s.eventId IS NULL''',
            (event_id,)
        )
        return cursor.fetchall()

    def create(self, name):
        cursor = self.db.connection.cursor()
        cursor.execute('''INSERT INTO player (name) VALUES (%s)''', (name,))
        self.db.connection.commit()
        return cursor.lastrowid
