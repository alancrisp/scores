import unittest

from scores.repo.scorerepo import ScoreRepo
from unittest.mock import MagicMock
from unittest.mock import call
from unittest.mock import patch

class ScoreRepoTestCase(unittest.TestCase):
    def setUp(self):
        self.db_patcher = patch('flask_mysqldb.MySQL')
        self.db = self.db_patcher.start()
        self.repo = ScoreRepo(self.db)

    def tearDown(self):
        self.db_patcher.stop()

    def test_creates_scores(self):
        self.db.connection.cursor().execute = MagicMock()
        self.repo.create(1, 2, {'1': 3, '2': 5})
        query = 'INSERT INTO score (eventId, playerId, hole, score) VALUES (%s, %s, %s, %s)'
        expected = [call(query, (1, 2, 1, 3)), call(query, (1, 2, 2, 5))]
        self.assertEqual(self.db.connection.cursor().execute.call_args_list, expected)
        self.db.connection.commit.assert_called_once()

    def test_gets_by_event(self):
        scores = [
            {
                'playerId': 1,
                'name': 'Joe Bloggs',
                'hole': 1,
                'score': 3,
            },
            {
                'playerId': 1,
                'name': 'Joe Bloggs',
                'hole': 2,
                'score': 5,
            },
            {
                'playerId': 2,
                'name': 'Erin Stone',
                'hole': 1,
                'score': 2,
            },
            {
                'playerId': 2,
                'name': 'Erin Stone',
                'hole': 2,
                'score': 4,
            },
        ]

        expected = {
            "Joe Bloggs": {
                1: 3,
                2: 5,
            },
            "Erin Stone": {
                1: 2,
                2: 4,
            },
        }

        self.db.connection.cursor().fetchall = MagicMock(return_value=scores)
        self.assertEqual(expected, self.repo.get_by_event(2))

if __name__ == '__main__':
    unittest.main()
