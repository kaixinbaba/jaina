import os

from cmd.common import Command


class ClearCommand(Command):
    """
    [green]Clear the screen, return to the first line.[/green]

    [blue]Usage:
    \[jaina] clear[/blue]
    """

    def process(self, cmd_arg, cli):
        # TODO if windows
        os.system('clear')

    def parse_tokens(self, tokens):
        pass
