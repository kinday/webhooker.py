from easydict import EasyDict as edict
from netaddr import IPAddress, IPNetwork
from operator import or_, eq
import json
import subprocess
import web


# branch_affected :: ([dict] -> string) -> boolean
# Returns true if any change affects specified branch
def branch_affected(changes, name):
    reducer = lambda affects, change: or_(affects, eq(change.new.name, name))
    return reduce(reducer, changes, False)

# in_networks :: ([IPNetwork] -> IPAddress|string) -> boolean
# Returns true if specified IP matches any network
def in_networks(networks, ip):
    reducer = lambda in_any, network: or_(in_any, ip in network)
    return reduce(reducer, networks, False)

# trigger_deployment :: string -> process
# Runs deploy command at given CWD
def trigger_deployment(path):
    cmd = ['fab', 'deploy']
    return subprocess.Popen(cmd, cwd=path)


whitelist = [
IPNetwork('127.0.0.1/8'),
IPNetwork('104.192.143.0/24'),
IPNetwork('131.103.20.160/27'),
IPNetwork('165.254.145.0/26'),
]


urls = ('/(.*)', 'handler')


class handler:
    def POST(self):
        if in_networks(whitelist, web.ctx.ip):
            data = edict(json.loads(web.data()))
            if branch_affected(data.push.changes, 'master'):
                trigger_deployment('/var/www/test')
            return 'OK'
        else:
            raise web.unauthorized()


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
