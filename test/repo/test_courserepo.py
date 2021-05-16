import unittest

from scores.repo.courserepo import CourseRepo
from unittest.mock import MagicMock
from unittest.mock import patch

class CourseRepoTestCase(unittest.TestCase):
    def setUp(self):
        self.db_patcher = patch('flask_mysqldb.MySQL')
        self.db = self.db_patcher.start()
        self.repo = CourseRepo(self.db)

    def tearDown(self):
        self.db_patcher.stop()

    def test_gets_all(self):
        courses = [
            {
                "courseId": 1,
                "name": "Test Course #1",
                "holes": 18,
            },
            {
                "courseId": 2,
                "name": "Test Course #2",
                "holes": 9,
            },
        ]

        self.db.connection.cursor().fetchall = MagicMock(return_value=courses)
        self.assertEqual(courses, self.repo.get_all())

    def test_gets_by_id(self):
        course = {
            "courseId": 1,
            "name": "Test Course #1",
        }

        self.db.connection.cursor().fetchone = MagicMock(return_value=course)
        self.assertEqual(course, self.repo.get_by_id(1))

    def test_gets_menu_options(self):
        options = [
            {"courseId": 1, "name": "Test Course #1"},
            {"courseId": 2, "name": "Test Course #2"},
        ]

        self.db.connection.cursor().fetchall = MagicMock(return_value=options)
        self.assertEqual(options, self.repo.get_menu_options())

    def test_creates_course(self):
        self.repo.create('Test Course #3', 'Somewhere', 'Sheffield', 18)
        self.db.connection.cursor().execute.assert_called_with(
            'INSERT INTO course (name, location, city, holes) VALUES (%s, %s, %s, %s)',
            ('Test Course #3', 'Somewhere', 'Sheffield', 18)
        )
