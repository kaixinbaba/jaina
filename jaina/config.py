import json
import os

DEFAULT_CONFIG_PATH = '.jaina'
DEFAULT_CONFIG_FILE = 'config.json'

home_path = os.environ['HOME']
config_path = os.path.join(home_path, DEFAULT_CONFIG_PATH)
if not os.path.exists(config_path):
    os.mkdir(config_path)

config_file_path = os.path.join(config_path, DEFAULT_CONFIG_FILE)
config_content = open(config_file_path, 'r').read()
if not config_content:
    # TODO default config file content
    open(config_file_path, 'w').write("{}")


class Config(object):

    def __init__(self, hosts, **kwargs):
        self.hosts = hosts

    def __str__(self):
        return f'Config: hosts=' + str(self.hosts)

    def __repr__(self):
        return self.__str__()


def parse_config(**kwargs):
    # 命令行优先
    kw_file = json.loads(open(os.path.join(config_path, DEFAULT_CONFIG_FILE)).read())
    kw_file.update(kwargs)
    return Config(**kw_file)
