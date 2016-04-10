from ..ip import to_networks
from netaddr import IPNetwork
import unittest


class TestToNetworks(unittest.TestCase):
    fixtures = ['127.0.0.1/8']

    def test_to_networks(self):
        networks = to_networks(self.fixtures)
        self.assertTrue(isinstance(networks[0], IPNetwork))
