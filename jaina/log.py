from rich.console import Console

from banner import banner as ban, word
from view.common import *

console = Console()


def log(s):
    console.print(s)


def debug(s):
    console.print(gray(s))


def info(s):
    console.print(green(s))


def warn(s):
    console.print(yellow(s))


def error(s):
    console.print(red(s))


def banner():
    console.print(blue(ban))
    console.print(green(word))
