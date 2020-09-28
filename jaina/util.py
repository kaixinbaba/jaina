import os

import time


def cmd(s):
    return os.popen(s).read()


def merge_path(parent_path, path):
    if not parent_path:
        return get_path(path)
    else:
        return ('' if parent_path == '/' else parent_path) + get_path(path)


def get_relative_new_path(chroot, path):
    path_split = path.split('/')
    chroot_split = chroot.split('/')
    # 弹出第一个空字符串
    chroot_split.pop(0)

    for p in path_split:
        if p == '..':
            if len(chroot_split) > 0:
                chroot_split.pop()
        elif p == '.':
            continue
        else:
            chroot_split.append(p)
    new_path = merge_path('/', '/'.join(chroot_split))
    return new_path


def get_path(path):
    if path.startswith('/'):
        return path
    else:
        return '/' + path


stat_fields = [
    'czxid',
    'mzxid',
    'ctime',
    'mtime',
    'version',
    'cversion',
    'aversion',
    'ephemeralOwner',
    'dataLength',
    'numChildren',
    'pzxid',
]

stat_max_field_len = sorted(map(lambda x: len(x), stat_fields))[-1]


def filter_stat_fields(f):
    return f in stat_fields


def timestamp2datetime(ts):
    # FIXME mtime要除以1000，如果其他的情况不需要这么做呢
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts / 1000))


def get_stat_value(r, f):
    if f == 'mtime':
        return timestamp2datetime(getattr(r, f))
    else:
        return getattr(r, f)


def get_stat_content(stat, data=None):
    c = []
    if data:
        c.append(f"'{data.decode()}'")
    for f in filter(filter_stat_fields, dir(stat)):
        v = get_stat_value(stat, f)
        c.append(f'{f.ljust(stat_max_field_len, " ")} = {v}')
    return '\n'.join(c)
