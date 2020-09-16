import importlib
import os
import re

from exception import CommandNotExistsException


def register_cmd():
    d = {}
    for file_name in filter(lambda f: (f != '__init__.py' and f.endswith('_.py')),
                            os.listdir(os.path.join(os.path.dirname(__file__), 'cmd'))):
        file_name = file_name[:-3]
        py = importlib.import_module('cmd.' + file_name)
        for class_name in filter(lambda f: f.endswith('Command') and f != 'Command', dir(py)):
            # 把后缀下划线去掉, 并且创建命令实例
            d[file_name[:-1]] = getattr(py, class_name)()
    return d


cmd_dict = register_cmd()


def handle_input(text):
    tokens = re.split(r'\s+', text)
    first_token = tokens[0]
    cmd = cmd_dict.get(first_token)
    if cmd is None:
        raise CommandNotExistsException(f'The command \'{first_token}\' not exists!')
    cmd_arg = cmd.parse_tokens(tokens)
    cmd.process(cmd_arg)
