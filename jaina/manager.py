import importlib
import os

from prompt_toolkit.completion import WordCompleter


def register(package, class_filter):
    d = {}
    for file_name in filter(lambda f: (f != '__init__.py' and f != 'kaixin_.py' and f.endswith('_.py')),
                            os.listdir(os.path.join(os.path.dirname(__file__), package))):
        file_name = file_name[:-3]
        py = importlib.import_module(package + '.' + file_name)
        key = file_name[:-1]
        if key == 'os':
            # os特殊处理下
            key = '!'
        for class_name in filter(class_filter, dir(py)):
            d[key] = getattr(py, class_name)()
    return d


def register_cmd():
    return register('cmd', lambda f: f.endswith('Command') and f != 'Command')


cmd_dict = register_cmd()


def register_view():
    return register('view', lambda f: f.endswith('ViewHandler') and f != 'ViewHandler')


view_dict = register_view()


completer = WordCompleter(list(cmd_dict.keys()), ignore_case=True)