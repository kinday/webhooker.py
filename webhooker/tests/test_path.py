from ..utils import path
import unittest


class TestPath(unittest.TestCase):
    fixtures = {'foo': {'bar': 1}}

    def test_get_value(self):
        self.assertEqual(
            path(['foo', 'bar'], self.fixtures),
            1,
        )

    def test_wrong_path(self):
        self.assertEqual(
            path(['foo', 'baz'], self.fixtures),
            None,
        )

    def test_handle_going_too_deep(self):
        self.assertEqual(
            path(['foo', 'bar', 'baz'], self.fixtures),
            None,
        )
