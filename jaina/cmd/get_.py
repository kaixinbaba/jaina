from optparse import OptionParser

from kazoo.exceptions import NoNodeError

from cmd.common import Command, default_watch
from util import filter_stat_fields, timestamp2datetime, stat_max_field_len, get_stat_value, get_stat_content
from view.plain_ import PlainViewModel


class GetCommand(Command):
    """
    [green]Get node information.[/green]
    [white]Try '[bold]get -h[/bold]' for more information about options.:smile:[/white]

    [blue]Example:
    (jaina) \[/] get /
    (jaina) \[/] get /your/path
    (jaina) \[/] get -w /your/need/watch/path
    [/blue]
    """

    def __init__(self, name):
        super().__init__(name)
        self.parser = OptionParser()
        self.parser.add_option("-w", "--watch",
                               action="store_true", dest="watch", default=False,
                               help="Add watch to the path, default False")

    def process(self, opt, arg, cli):
        path = arg[1]
        try:
            data, stat = cli.client.get(path, default_watch if opt.watch else None)
            return PlainViewModel(content=get_stat_content(stat, data), color='info')
        except NoNodeError as e:
            raise ValueError(f"Path '{path}' not exists")

    def post_validate(self, opt, arg):
        arg_len = len(arg)
        if arg_len > 2:
            raise ValueError("get 'path' is required")
        if arg_len < 2:
            arg.append('')

    def alias_list(self):
        return ['g']

