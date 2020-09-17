import os


def cmd(s):
    return os.popen(s).read()