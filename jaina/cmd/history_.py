from optparse import OptionParser

from cmd.common import Command
from view.plain_ import PlainViewModel


class HistoryCommand(Command):
    """
    [green]Display command history list.[/green]
    [white]Try '[bold]history -h[/bold]' for more information about options.:smile:[/white]

    [blue]Example:
    (jaina) \[/] history
    (jaina) \[/] history -l 500
    [/blue]
    """

    def __init__(self, name):
        super().__init__(name)
        self.parser = OptionParser()
        self.parser.add_option("-l", "--limit",
                               action="store", type=int, dest="limit", default=500,
                               help="return the limit of history, default 500")

    def post_validate(self, opt, arg):
        if opt.limit > 5000:
            raise ValueError('Max limit is 5000!')
        if opt.limit < 1:
            raise ValueError('Min limit is 1!')

    def process(self, opt, arg, cli):
        history_list = cli.history.read_history(opt.limit)
        return PlainViewModel(content='\n'.join(history_list), color='info')


