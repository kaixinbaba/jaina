import os
import sys

import click
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style

from exception import CommandNotExistsException
from history import History

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from info import __version__
import log
from cli import Cli
from term import handle_input
from config import parse_config, jaina_home_path
from manager import completer
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.history import FileHistory


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    log.info(__version__)
    ctx.exit()


def handle_exception(e, config):
    if isinstance(e, (EOFError, KeyboardInterrupt)):
        return True
    if config.debug:
        log.console.print_exception()
    else:
        log.error(e)
    if isinstance(e, CommandNotExistsException):
        log.warn('Please input \'help\' or \'help <command>\' to get more info.')


def loop_prompt(cli, config):
    session = PromptSession(
        completer=completer,
        style=Style.from_dict({
            'completion-menu.completion': 'bg:#FFB6C1 #000000',
            'completion-menu.completion.current': 'bg:#82B22C #ffffff',
            'scrollbar.background': 'bg:#88aaaa',
            'scrollbar.button': 'bg:#222222',
        }),
        auto_suggest=AutoSuggestFromHistory(),
        complete_in_thread=True,
        history=FileHistory(os.path.join(jaina_home_path, 'history')),
    )
    cli.history = History()
    while True:
        try:
            text = session.prompt(f'(jaina) [{cli.chroot}] ')
            if text:
                handle_input(text, cli)
        except Exception as e:
            if handle_exception(e, config):
                break


@click.command()
@click.option('-h', '--hosts', default='127.0.0.1:2181',
              help="""The ZK server list\n
              ip1:port1\n
              ip1:port1/chroot\n
              ip1:port1,ip2:port2\n
              ip1:port1,ip2:port2/chroot\n
              """)
@click.option('--debug/--no-debug', default=False)
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True, help='show version')
@click.pass_context
def main(ctx, hosts, debug):
    """A Powerful Zookeeper Client Tool."""
    cli = None
    try:
        # 解析参数
        config = parse_config(hosts=hosts, debug=debug)
        # 创建客户端
        cli = Cli(config=config)
        cli.connect()
        log.banner()
        # 进入交互界面
        loop_prompt(cli, config)
    except Exception as e:
        log.error(e)
        ctx.exit(code=1)
    finally:
        if cli:
            cli.quit()
        log.info('BYE!')


if __name__ == '__main__':
    main()
