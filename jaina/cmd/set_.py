from optparse import OptionParser

from kazoo.exceptions import NoNodeError, BadVersionError

from cmd.common import Command
from view.plain_ import PlainViewModel


class SetCommand(Command):
    """
    [green]Set a value for a node.[/green]
    [white]Try '[bold]set -h[/bold]' for more information about options.:smile:[/white]

    [blue]Example:
    (jaina) [/] set /test abc
    (jaina) [/] set -v 1 /test abc
    [/blue]
    """

    def __init__(self):
        self.parser = OptionParser()
        self.parser.add_option("-v", "--version",
                               action="store", type=int, dest="version", default=-1,
                               help="Version requirements of the target node, any if -1, default -1")

    def process(self, opt, arg, cli):
        try:
            cli.client.set(arg[1], arg[2].encode(), version=opt.version)
            return PlainViewModel(content=f'[green]set data ok[/green]')
        except NoNodeError as e:
            raise ValueError(f"The path '{arg[1]}' not exists")
        except BadVersionError as e:
            raise ValueError(f"The specified version '{opt.version}' does not match")

    def post_validate(self, opt, arg):
        arg_len = len(arg)
        if arg_len > 3:
            raise ValueError("set command required 'path' and 'value'")
        if arg_len < 3:
            arg.append('')



