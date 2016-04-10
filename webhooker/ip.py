from .utils import any_pass
from netaddr import IPAddress, IPNetwork
from operator import contains


# in_networks :: ([IPNetwork] -> string) -> boolean
# Returns true if specified IP matches any network
def in_networks(networks, ip_str):
    ip = IPAddress(ip_str)
    return any_pass(lambda network: contains(network, ip), networks)


# to_networks :: [string] -> [IPNetwork]
# Converts list of strings to array of IP networks
def to_networks(ip_list):
    return map(IPNetwork, ip_list)
