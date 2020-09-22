from optparse import OptionParser

from kazoo.exceptions import NoNodeError

from cmd.common import Command, default_watch
from util import filter_stat_fields, timestamp2datetime, stat_max_field_len
from view.plain_ import PlainViewModel


class GetCommand(Command):
    """
    [green]Get node information.[/green]
    [white]Try '[bold]get -h[/bold]' for more information about options.:smile:[/white]

    [blue]Example:
    \[jaina] get /
    \[jaina] get /your/path
    \[jaina] get -w /your/need/watch/path
    [/blue]
    """

    def __init__(self):
        self.parser = OptionParser()
        self.parser.add_option("-w", "--watch",
                               action="store_true", dest="watch", default=False,
                               help="Add watch to the path, default False")

    def process(self, opt, arg, cli):
        path = arg[1]
        try:
            data, stat = cli.client.get(path, default_watch if opt.watch else None)
            content = [f'{path.ljust(stat_max_field_len, " ")} = \'{data.decode()}\'']
            for f in filter(filter_stat_fields, dir(stat)):
                v = getattr(stat, f)
                if f.endswith('time'):
                    v = timestamp2datetime(v)
                content.append(f'{f.ljust(stat_max_field_len, " ")} = {v}')
            return PlainViewModel(content='\n'.join(content), color='info')
        except NoNodeError as e:
            raise ValueError(f"Path '{path}' not exists")

    def post_validate(self, opt, arg):
        if len(arg) != 2:
            raise ValueError('Get path is required')
