import os
import sys

import click
from prompt_toolkit import PromptSession

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from info import __version__
import log
from cli import Cli
from term import handle_input


class Config(object):

    def __init__(self, hosts):
        self.hosts = hosts

    def __str__(self):
        return f'Config: hosts=' + str(self.hosts)

    def __repr__(self):
        return self.__str__()


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    log.info(__version__)
    ctx.exit()


def parse_config(hosts=None):
    return Config(hosts=hosts)


def loop_prompt():
    session = PromptSession()
    while True:
        try:
            text = session.prompt('[jaina] ')
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        else:
            handle_input(text)


@click.command()
@click.option('-h', '--hosts', default='127.0.0.1:2181',
              help="""The ZK server list\n
              ip1:port1\n
              ip1:port1/chroot\n
              ip1:port1,ip2:port2\n
              ip1:port1,ip2:port2/chroot\n
              """)
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True, help='show version')
@click.pass_context
def main(ctx, hosts):
    """A Powerful Zookeeper Client Tool."""
    try:
        # 解析参数
        config = parse_config(hosts=hosts)
        # 创建客户端
        cli = Cli(config=config)
        cli.connect()
        log.banner()
        # 进入交互界面
        loop_prompt()
    except Exception as e:
        log.error(e)
        ctx.exit(code=1)
    finally:
        if cli:
            cli.quit()
        log.info('BYE! Seeya')


if __name__ == '__main__':
    main()
