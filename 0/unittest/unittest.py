from form0 import db_query
import unittest


class testing(unittest.TestCase):
    def test_area(self):
        self.assertEqual(db_query("qwerty"), None)