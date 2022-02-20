import unittest

from scores.repo.playerrepo import PlayerRepo
from unittest.mock import MagicMock
from unittest.mock import PropertyMock
from unittest.mock import patch

class PlayerRepoTestCase(unittest.TestCase):
    def setUp(self):
        self.db_patcher = patch('flask_mysqldb.MySQL')
        self.db = self.db_patcher.start()
        self.repo = PlayerRepo(self.db)

    def tearDown(self):
        self.db_patcher.stop()

    def test_gets_all(self):
        players = [
            {"playerId": 1, "name": "Joe Bloggs"},
            {"playerId": 2, "name": "Erin Stone"},
        ]

        self.db.connection.cursor().fetchall = MagicMock(return_value=players)
        self.assertEqual(players, self.repo.get_all())

    def test_gets_by_id(self):
        player = {"playerId": 1, "name": "Joe Bloggs"}
        self.db.connection.cursor().fetchone = MagicMock(return_value=player)
        self.assertEqual(player, self.repo.get_by_id(1))

    def test_gets_menu_options_for_event(self):
        players = [
            {"playerId": 1, "name": "Joe Bloggs"},
            {"playerId": 2, "name": "Erin Stone"},
        ]

        self.db.connection.cursor().fetchall = MagicMock(return_value=players)
        self.assertEqual(players, self.repo.get_menu_options_for_event(1))

    def test_creates_player(self):
        self.repo.create('Joe Bloggs')
        self.db.connection.cursor().execute.assert_called_with(
            'INSERT INTO player (name) VALUES (%s)',
            ('Joe Bloggs',)
        )
        self.db.connection.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
