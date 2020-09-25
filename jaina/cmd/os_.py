import log
from cmd.common import Command
from util import cmd


class OsCommand(Command):
    """
    [green]Use the '!' prefix to directly call the operating system commands.[/green]

    [blue]Example:
    (jaina) \[/] !ls -l /your/target/path
    (jaina) \[/] !clear
    (jaina) \[/] !pwd
    [/blue]
    """

    def __init__(self, name):
        super().__init__(name)

    def process(self, opt, arg, cli):
        # FIXME cd 命令不会生效，我看了下ipython中也一样，所以就不处理了
        log.log(cmd(' '.join(arg)))

    def parse_tokens(self, tokens):
        # 去除感叹号
        tokens[0] = tokens[0][1:]
        return None, tokens
