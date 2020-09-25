from optparse import OptionParser

from cmd.common import Command, default_watch
from util import filter_stat_fields, timestamp2datetime
from view.plain_ import PlainViewModel


class ExistsCommand(Command):
    """
    [green]Check if the specified path exists.[/green]
    [white]Try '[bold]exists -h[/bold]' for more information about options.:smile:[/white]

    [blue]Example:
    (jaina) [/] exists /your/path
    (jaina) [/] exists -s /need/stat/path
    (jaina) [/] exists -w /your/need/watch/path
    [/blue]
    """

    def __init__(self):
        self.parser = OptionParser()
        self.parser.add_option("-s", "--stat",
                               action="store_true", dest="stat", default=False,
                               help="Also show the path statistics info, default False")
        self.parser.add_option("-w", "--watch",
                               action="store_true", dest="watch", default=False,
                               help="Add watch to the path, default False")

    def _get_stat_value(self, r, f):
        if f == 'mtime':
            return timestamp2datetime(getattr(r, f))
        else:
            return getattr(r, f)

    def process(self, opt, arg, cli):
        if len(arg) == 1 or not arg[1]:
            raise ValueError('<path> is required, use -h to get help')
        r = cli.client.exists(arg[1], default_watch if opt.watch else None)
        if r is None:
            content = False
        elif opt.stat:
            content = '\n'.join([f'{f}={self._get_stat_value(r, f)}' for f in filter(filter_stat_fields, dir(r))])
        else:
            content = True

        return PlainViewModel(content=content)




