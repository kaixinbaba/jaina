from abc import ABCMeta, abstractmethod


def red(s):
    return color(s, 'red')


def green(s):
    return color(s, 'green')


def yellow(s):
    return color(s, 'yellow')


def gray(s):
    return color(s, 'gray')


def blue(s):
    return color(s, 'blue')


def purple(s):
    return color(s, 'purple')


def white(s):
    return color(s, 'white')


def color(s, c):
    return f'[{c}]{s}[/{c}]'


class ViewHandler(metaclass=ABCMeta):

    @abstractmethod
    def handle(self, view_model):
        pass


class ViewModel(metaclass=ABCMeta):

    @property
    def name(self):
        return type(self).__name__.replace('ViewModel', '').lower()
