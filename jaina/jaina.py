import os
import sys

import click
from prompt_toolkit import PromptSession

from exception import CommandNotExistsException

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from info import __version__
import log
from cli import Cli
from term import handle_input
from config import parse_config


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    log.info(__version__)
    ctx.exit()


def handle_exception(e):
    if isinstance(e, (EOFError, KeyboardInterrupt)):
        return True
    log.error(e)
    if isinstance(e, CommandNotExistsException):
        log.warn('Please input \'help\' to get more info')


def loop_prompt():
    session = PromptSession()
    while True:
        try:
            text = session.prompt('[jaina] ')
            handle_input(text)
        except Exception as e:
            if handle_exception(e):
                break


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
    cli = None
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
        log.info('BYE!')


if __name__ == '__main__':
    main()
