from ..utils import any_pass
from functools import partial
from operator import eq
import unittest


class TestAnyPass(unittest.TestCase):
    fixtures = [1, 2, 3]

    def test_anything_passes(self):
        self.assertTrue(any_pass(partial(eq, 2), self.fixtures))

    def test_nothing_passes(self):
        self.assertFalse(any_pass(partial(eq, 6), self.fixtures))
