import json
import time
import subprocess
from os import path

from setting import RETRY_COUNTS, RETRY_INTERVAL


def _file(f):
    return path.join(_base(), '../../{}'.format(f))


def _base():
    return path.dirname(__file__)


def _bin():
    c = _file('bin/longhorn')
    assert path.exists(c)
    return c


def info_get(url):
    cmd = [_bin(), '--url', url, '--debug', 'info']
    return json.loads(subprocess.check_output(cmd))


def snapshot_create(url):
    cmd = [_bin(), '--url', url, '--debug', 'snapshot', 'create']
    return subprocess.check_output(cmd).strip()


def snapshot_rm(url, name):
    cmd = [_bin(), '--url', url, '--debug', 'snapshot', 'rm', name]
    subprocess.check_call(cmd)


def snapshot_revert(url, name):
    cmd = [_bin(), '--url', url, '--debug', 'snapshot', 'revert', name]
    subprocess.check_call(cmd)


def snapshot_ls(url):
    cmd = [_bin(), '--url', url, '--debug', 'snapshot', 'ls']
    return subprocess.check_output(cmd)


def snapshot_info(url):
    cmd = [_bin(), '--url', url, '--debug', 'snapshot', 'info']
    output = subprocess.check_output(cmd)
    return json.loads(output)


def snapshot_purge(url):
    cmd = [_bin(), '--url', url, '--debug', 'snapshot', 'purge']
    return subprocess.check_call(cmd)


def backup_status(url, backupID):
    output = ""
    cmd = [_bin(), '--url', url, 'backup', 'status', backupID]
    for x in range(RETRY_COUNTS):
        backup = json.loads(subprocess.check_output(cmd).strip())
        if 'backupURL' in backup.keys():
            output = backup['backupURL']
            break
        elif 'backupError' in backup.keys():
            output = backup['backupError']
            break
        time.sleep(RETRY_INTERVAL)
    return output


def backup_create(url, snapshot, dest):
    cmd = [_bin(), '--url', url, '--debug',
           'backup', 'create', snapshot, '--dest', dest]
    return backup_status(url, subprocess.check_output(cmd).strip())


def backup_rm(url, backup):
    cmd = [_bin(), '--url', url, '--debug', 'backup', 'rm', backup]
    return subprocess.check_call(cmd)


def backup_restore(url, backup):
    cmd = [_bin(), '--url', url, '--debug', 'backup', 'restore', backup]
    return subprocess.check_output(cmd).strip()


def backup_inspect(url, backup):
    cmd = [_bin(), '--url', url, '--debug', 'backup', 'inspect', backup]
    return json.loads(subprocess.check_output(cmd))


def add_replica(url, replica_url):
    cmd = [_bin(), '--url', url, '--debug', 'add', replica_url]
    return subprocess.check_output(cmd).strip()


def restore_to_file(url, backup_url,
                    backing_file='', output_file='', format=''):
    cmd = [_bin(), '--url', url, '--debug',
           'backup', 'restore-to-file', backup_url]
    if backing_file:
        cmd.append('--backing-file')
        cmd.append(backing_file)
    if output_file:
        cmd.append('--output-file')
        cmd.append(output_file)
    if format:
        cmd.append('--output-format')
        cmd.append(format)
    return subprocess.check_output(cmd)


def restore_inc(url, backup_url, last_restored):
    cmd = [_bin(), '--url', url, '--debug', 'backup', 'restore',
           backup_url, '--incrementally', '--last-restored', last_restored]
    return subprocess.check_output(cmd)


def sync_agent_server_reset(url):
    cmd = [_bin(), '--url', url, '--debug', 'sync-agent-server-reset']
    return subprocess.check_output(cmd)


def restore_status(url):
    cmd = [_bin(), '--url', url, '--debug', 'backup', 'restore-status']
    return json.loads(subprocess.check_output(cmd))
