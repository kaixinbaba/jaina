from rich import print

from banner import banner as ban, word
from view.common import *


def log(s):
    print(s)


def debug(s):
    print(gray(s))


def info(s):
    print(green(s))


def warn(s):
    print(yellow(s))


def error(s):
    print(red(s))


def banner():
    print(blue(ban))
    print(green(word))
