from functools import partial
from netaddr import IPAddress, IPNetwork
from operator import contains, eq, or_
from urlparse import parse_qs
import json
import subprocess
import web


# any_pass :: (fn -> [*]) -> boolean
# Returns True if any iterable item returns true when passed to fn
def any_pass(fn, iterable):
    return reduce(lambda passed, a: or_(passed, fn(a)), iterable, False)


# branch_affected :: ([dict] -> string) -> boolean
# Returns true if any change affects specified branch
def branch_affected(changes, name):
    get_name = partial(path, ['new', 'name'])
    return any_pass(lambda change: eq(name, get_name(change)), changes)


# in_networks :: ([IPNetwork] -> string) -> boolean
# Returns true if specified IP matches any network
def in_networks(networks, ip_str):
    ip = IPAddress(ip_str)
    return any_pass(lambda network: contains(network, ip), networks)


# path :: ([string] -> dict) -> *
# Gets deep value from dict
def path(keys, dict_):
    return reduce(
        lambda v, k: v and isinstance(v, dict) and v.get(k) or None,
        keys,
        dict_
    )


# trigger_deployment :: string -> process
# Runs deploy command at given CWD
def trigger_deployment(path):
    cmd = ['fab', 'deploy']
    return subprocess.Popen(cmd, cwd=path)


# List of allowed IP addresses
whitelist = [
    # Allow localhost
    IPNetwork('127.0.0.1/8'),

    # Allow Bitbucket
    IPNetwork('104.192.143.0/24'),
    IPNetwork('131.103.20.160/27'),
    IPNetwork('165.254.145.0/26'),
]


urls = ('/(.*)', 'handler')


class handler:

    def POST(self, project):
        get_changes = partial(path, ['push', 'changes'])

        if in_networks(whitelist, web.ctx.ip):
            data = json.loads(web.data())
            query = parse_qs(web.ctx.query[1:])
            branch = query.get('branch', ['master'])[0]

            if branch_affected(get_changes(data), branch):
                trigger_deployment('/var/www/{0!s}'.format(project))

            return 'OK'

        else:
            raise web.unauthorized()


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()