import log
from cmd.common import Command
from util import cmd


class OsCommand(Command):
    """
    [green]Use the '!' prefix to directly call the operating system commands.[/green]

    [blue]Usage:
    \[jaina] !ls -l /your/target/path
    \[jaina] !clear
    \[jaina] !pwd
    [/blue]
    """

    def process(self, cmd_arg, cli):
        # FIXME cd 命令不会生效，我看了下ipython中也一样，所以就不处理了
        log.log(cmd(' '.join(cmd_arg)))

    def parse_tokens(self, tokens):
        # 去除感叹号
        tokens[0] = tokens[0][1:]
        return tokens
