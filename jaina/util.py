import os

import time


def cmd(s):
    return os.popen(s).read()


def merge_path(parent_path, path):
    if not parent_path:
        return get_path(path)
    else:
        return ('' if parent_path == '/' else parent_path) + get_path(path)


def get_path(path):
    if path.startswith('/'):
        return path
    else:
        return '/' + path


stat_fields = ['czxid', 'mzxid', 'ctime', 'mtime', 'version', 'cversion', 'aversion',
               'ephemeralOwner', 'dataLength', 'numChildren', 'pzxid']


def filter_stat_fields(f):
    return f in stat_fields


def timestamp2datetime(ts):
    # FIXME mtime要除以1000，如果其他的情况不需要这么做呢
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts / 1000))
