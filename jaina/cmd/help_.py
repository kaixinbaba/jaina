from optparse import OptionParser

from cmd.common import Command
from view.plain_ import PlainViewModel


class HelpCommand(Command):
    """
    [green]Show all built-in command.[/green]

    [blue]Usage:
    \[jaina] help[/blue]
    """

    def __init__(self):
        self.parser = OptionParser()

    def process(self, cmd_arg, cli):
        # FIXME lazy import
        from manager import cmd_dict
        if len(cmd_arg[1]) == 1:
            # just help
            all_cmd = '\n'.join(sorted(cmd_dict.keys()))
            return PlainViewModel(content=f"[green]{all_cmd}[/green]\nTry to use 'help <command>' get more info.\n")
        else:
            cmd = cmd_arg[1][1]
            if cmd not in cmd_dict:
                raise ValueError(f'Can\'t find the \'{cmd}\' command')
            return PlainViewModel(content=cmd_dict[cmd].__doc__)

    def parse_tokens(self, tokens):
        if len(tokens) > 2:
            raise ValueError('The help command can only accept at most one <command>')
        return self.parser.parse_args(tokens)
