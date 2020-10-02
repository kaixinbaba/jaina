from optparse import OptionParser

from cmd.common import Command
from view.plain_ import PlainViewModel


class HistoryCommand(Command):
    """
    [green]Display command history list.[/green]
    [white]Try '[bold]history -h[/bold]' for more information about options.:smile:[/white]

    [blue]Example:
    (jaina) \[/] history
    (jaina) \[/] history -t
    [/blue]
    """

    def __init__(self, name):
        super().__init__(name)
        self.parser = OptionParser()
        self.parser.add_option("-t", "--time",
                               action="store_true", dest="time", default=False,
                               help="Display history with datetime, default False")

    def process(self, opt, arg, cli):
        history_list = cli.history.read_history(opt.time)
        return PlainViewModel(content='\n'.join(history_list), color='info')
