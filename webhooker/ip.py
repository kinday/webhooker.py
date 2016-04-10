from .utils import any_pass
from netaddr import IPAddress
from operator import contains


# in_networks :: ([IPNetwork] -> string) -> boolean
# Returns true if specified IP matches any network
def in_networks(networks, ip_str):
    ip = IPAddress(ip_str)
    return any_pass(lambda network: contains(network, ip), networks)
