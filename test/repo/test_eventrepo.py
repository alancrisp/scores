import unittest

from scores.repo.eventrepo import EventRepo
from unittest.mock import MagicMock
from unittest.mock import patch

class EventRepoTestCase(unittest.TestCase):
    def setUp(self):
        self.db_patcher = patch('flask_mysqldb.MySQL')
        self.db = self.db_patcher.start()
        self.repo = EventRepo(self.db)

    def tearDown(self):
        self.db_patcher.stop()

    def test_gets_all(self):
        events = [
            {
                "eventId": 1,
                "name": "Test Event #1",
            },
            {
                "eventId": 2,
                "name": "Test Event #2",
            },
        ]

        self.db.connection.cursor().fetchall = MagicMock(return_value=events)
        self.assertEqual(events, self.repo.get_all())

    def test_gets_by_id(self):
        event = {
            "eventId": 1,
            "name": "Test Event #1",
        }

        self.db.connection.cursor().fetchone = MagicMock(return_value=event)
        self.assertEqual(event, self.repo.get_by_id(1))

    def test_creates_event(self):
        self.repo.create(1, '2021-01-15')
        self.db.connection.cursor().execute.assert_called_with(
            'INSERT INTO event (courseId, eventDate) VALUES (%s, %s)',
            (1, '2021-01-15')
        )
        self.db.connection.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
