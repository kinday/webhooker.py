from functools import partial
from netaddr import IPNetwork
from operator import eq
from webhooker import any_pass, branch_affected, in_networks, path
import json
import unittest

class TestWebhooker(unittest.TestCase):

    def test_any_pass(self):
        fixtures = [1, 2, 3]

        self.assertEqual(
            any_pass(partial(eq, 2), fixtures),
            True,
            'should return True when any item passes',
        )

        self.assertEqual(
            any_pass(partial(eq, 6), fixtures),
            False,
            'should return False when no items pass',
        )


    def test_branch_affected(self):
        fixtures = [
            {'new': {'name': 'master'}},
            {'new': {'name': 'develop'}},
        ]

        self.assertEqual(
            branch_affected(fixtures, 'master'),
            True,
            'should return True when branch is affected',
        )

        self.assertEqual(
            branch_affected(fixtures, 'feature/foo'),
            False,
            'should return False when branch is not affected',
        )


    def test_in_networks(self):
        fixtures = [
            # Allow localhost
            IPNetwork('127.0.0.1/8'),
        ]

        self.assertEqual(
            in_networks(fixtures, '127.0.0.1'),
            True,
            'should return True when IP is in networks',
        )

        self.assertEqual(
            in_networks(fixtures, '192.168.1.1'),
            False,
            'should return False when IP is not in networks',
        )


    def test_path(self):
        fixtures = {'foo': {'bar': 1}}

        self.assertEqual(
            path(['foo', 'bar'], fixtures),
            1,
            'should get value',
        )

        self.assertEqual(
            path(['foo', 'baz'], fixtures),
            None,
            'should return None',
        )

        self.assertEqual(
            path(['foo', 'bar', 'baz'], fixtures),
            None,
            'should not get if not dict',
        )


if __name__ == '__main__':
    unittest.main()
