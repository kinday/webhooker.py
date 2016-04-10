from .. import branch_affected
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


if __name__ == '__main__':
    unittest.main()
