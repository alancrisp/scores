from flask_mysqldb import MySQL

class ScoreRepo:
    def __init__(self, db: MySQL):
        self.db = db

    def create(self, event_id, player_id, scores):
        cursor = self.db.connection.cursor()
        query = '''INSERT INTO score (eventId, playerId, hole, score) VALUES (%s, %s, %s, %s)'''
        for hole, score in scores.items():
            cursor.execute(query, (event_id, player_id, int(hole), score,))
        self.db.connection.commit()

    """
    Returns a multidimensional dictionary indexed by player ID containing event scores
    """
    def get_by_event(self, event_id):
        cursor = self.db.connection.cursor()
        cursor.execute('SELECT s.playerId, p.name, s.hole, s.score FROM score s INNER JOIN player p USING (playerId) WHERE s.eventId = %s GROUP BY s.playerId, s.hole, s.score ORDER BY s.hole ASC', (event_id,))
        result = cursor.fetchall()
        scores = {}
        for row in result:
            scores.setdefault(row['name'], {})[row['hole']] = row['score']

        return scores
