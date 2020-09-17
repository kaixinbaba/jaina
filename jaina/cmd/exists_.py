from optparse import OptionParser

from cmd.common import Command


class ExistsCommand(Command):
    """
    [green]Check if the specified path exists.[/green]
    [white]Try '[bold]exists -h[/bold]' for more information about options.:smile:[/white]

    [blue]Example:
    \[jaina] exists /your/path
    \[jaina] ls -w /your/need/watch/path
    [/blue]
    """

    def __init__(self):
        self.parser = OptionParser()
        self.parser.add_option("-w", "--watch",
                               action="store_true", dest="watch", default=False,
                               help="Add watch to the path")

    def process(self, cmd_arg, cli):
        pass

