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


def color(s, c):
    return f'[{c}]{s}[/{c}]'
