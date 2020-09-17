import os


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
