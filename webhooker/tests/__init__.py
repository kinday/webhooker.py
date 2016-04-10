from .. import branch_affected, in_networks
from netaddr import IPNetwork
import unittest


class TestWebhooker(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
