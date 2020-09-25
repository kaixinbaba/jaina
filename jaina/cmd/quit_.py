from cmd.common import Command


class QuitCommand(Command):
    """
    [green]Quit jaina.[/green]
    [white]Try '[bold]quit -h[/bold]' for more information about options.:smile:[/white]

    [blue]Example:
    (jaina) \[/] quit
    [/blue]
    """

    def __init__(self, name):
        super().__init__(name)

    def process(self, opt, arg, cli):
        raise KeyboardInterrupt

    def alias_list(self):
        return ['close', 'bye', 'stop']


