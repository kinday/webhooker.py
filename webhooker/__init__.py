from .ip import in_networks
from .utils import any_pass, path
from functools import partial
from netaddr import IPAddress, IPNetwork
from operator import eq
from urlparse import parse_qs
import json
import subprocess
import web


# branch_affected :: ([dict] -> string) -> boolean
# Returns true if any change affects specified branch
def branch_affected(changes, name):
    get_name = partial(path, ['new', 'name'])
    return any_pass(lambda change: eq(name, get_name(change)), changes)


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
