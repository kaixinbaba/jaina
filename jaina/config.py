import json
import os

DEFAULT_CONFIG_PATH = '.jaina'
DEFAULT_CONFIG_FILE = 'config.json'

home_path = os.environ['HOME']
config_path = os.path.join(home_path, DEFAULT_CONFIG_PATH)
if not os.path.exists(config_path):
    os.mkdir(config_path)

config_file_path = os.path.join(config_path, DEFAULT_CONFIG_FILE)
config_content = open(config_file_path, 'r').read().strip()
if not config_content:
    # TODO default config file content
    open(config_file_path, 'w').write("{}")


class Config(object):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        s = ['Config:']
        for f in filter(lambda x: not x.startswith('__'), dir(self)):
            v = getattr(self, f)
            s.append(f'{f}={v}')
        return ' '.join(s)

    def __repr__(self):
        return self.__str__()


def parse_config(**kwargs):
    # 命令行优先
    kw_file = json.loads(open(os.path.join(config_path, DEFAULT_CONFIG_FILE)).read())
    kw_file.update(kwargs)
    return Config(**kw_file)
