import json
import os

DEFAULT_CONFIG_PATH = '.jaina'
DEFAULT_CONFIG_FILE = 'config.json'

home_path = os.environ['HOME']
jaina_home_path = os.path.join(home_path, DEFAULT_CONFIG_PATH)
if not os.path.exists(jaina_home_path):
    os.mkdir(jaina_home_path)

config_file_path = os.path.join(jaina_home_path, DEFAULT_CONFIG_FILE)
config_content = open(config_file_path, 'r').read().strip()
if not config_content:
    # TODO default config file content
    open(config_file_path, 'w').write("{}")


class Config(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__

    def __init__(self, **kwargs):
        super().__init__()
        for k, v in kwargs.items():
            self[k] = v

    def __str__(self):
        s = ['Config:']
        for k, v in self.items():
            s.append(f'{k}={v},')
        return ' '.join(s)[:-1]

    def __repr__(self):
        return self.__str__()

    def set(self, key, value):
        self[key] = value


def parse_config(**kwargs):
    # 命令行优先
    kw_file = json.loads(open(os.path.join(jaina_home_path, DEFAULT_CONFIG_FILE)).read())
    kw_file.update(kwargs)
    return Config(**kw_file)


def write_config(config):
    open(os.path.join(jaina_home_path, DEFAULT_CONFIG_FILE), 'w').write(json.dumps(config, indent=2))
