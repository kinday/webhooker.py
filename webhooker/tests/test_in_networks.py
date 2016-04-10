from ..ip import in_networks
from netaddr import IPNetwork
import unittest


class TestInNetworks(unittest.TestCase):
    fixtures = [IPNetwork('127.0.0.1/8')]

    def test_in_networks(self):
        self.assertTrue(in_networks(self.fixtures, '127.0.0.1'))

    def test_not_in_networks(self):
        self.assertFalse(in_networks(self.fixtures, '192.168.1.1'))
