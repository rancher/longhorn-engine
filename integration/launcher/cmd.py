import json
import subprocess
from os import path


LAUNCHER = "localhost:8500"
LONGHORN_BINARY = "./bin/longhorn"


def _bin():
    c = '/usr/local/bin/longhorn-engine-launcher'
    assert path.exists(c)
    return c


def launcher(url):
    return [_bin(), "--url", url]


def process_create(name, args,
                   url=LAUNCHER, binary=LONGHORN_BINARY):
    cmd = launcher(url) + ['process', 'create', '--name', name,
                           '--binary', binary, '--'] + args
    return json.loads(subprocess.check_output(cmd))


def process_delete(name, url=LAUNCHER):
    cmd = launcher(url) + ['process', 'delete', '--name', name]
    return json.loads(subprocess.check_output(cmd))


def process_get(name, url=LAUNCHER):
    cmd = launcher(url) + ['process', 'get', '--name', name]
    return json.loads(subprocess.check_output(cmd))


def process_list(url=LAUNCHER):
    cmd = launcher(url) + ['process', 'list']
    return json.loads(subprocess.check_output(cmd))
