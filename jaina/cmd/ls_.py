from collections import defaultdict
from optparse import OptionParser

from kazoo.exceptions import NoNodeError

from cmd.common import Command, default_watch
from util import merge_path
from view.tree_ import TreeViewModel


class LsCommand(Command):
    """
    [green]Display node information under the path.[/green]
    [white]Try '[bold]ls -h[/bold]' for more information about options.:smile:[/white]

    [blue]Example:
    \[jaina] ls /
    \[jaina] ls /your/path
    \[jaina] ls -s /your/path
    \[jaina] ls -s -w /your/need/watch/path
    \[jaina] ls -R /your/path
    [/blue]
    """

    def __init__(self):
        self.parser = OptionParser()
        self.parser.add_option("-s", "--stat",
                               action="store_true", dest="stat", default=False,
                               help="""Also show the path statistics info
                               version,cversion,aversion,mtime,numChildren, default False
                               """)
        self.parser.add_option("-w", "--watch",
                               action="store_true", dest="watch", default=False,
                               help="Add watch to the path, default False")
        self.parser.add_option("-R", "--recursion",
                               action="store_true", dest="recursion", default=False,
                               help="Recursively display all nodes under the path, default False")
        self.stat_width_fields = ['version', 'cversion', 'aversion', 'numChildren']

    def process(self, opt, arg, cli):
        path = self._check_arg(arg)
        stat_dict = {}
        stat_width = defaultdict(int)
        path_dict = self._collect_path(cli, path, opt, stat_dict, stat_width)
        return TreeViewModel(root_path=path, tree_dict={path: path_dict}, stat_dict=stat_dict, stat_width=stat_width)

    def _calculate_stat_width(self, stat, stat_width):
        for field in self.stat_width_fields:
            max_width = stat_width[field]
            width = len(str(getattr(stat, field)))
            if width > max_width:
                stat_width[field] = width

    def _collect_path(self, cli, path, opt, stat_dict, stat_width):
        d = {}
        # TODO kazoo没有ls命令，只有get_children替代，区别是get_children的watch有问题
        try:
            r = cli.client.get_children(path, default_watch if opt.watch else None, opt.stat)
        except NoNodeError as e:
            raise ValueError(f"Path '{path}' not exists")
        if isinstance(r, tuple):
            child_paths = r[0]
            stat = r[1]
        else:
            child_paths = r
            stat = None
        if stat:
            self._calculate_stat_width(stat, stat_width)
            stat_dict[path] = stat
        for child_path in child_paths:
            if opt.recursion:
                d[child_path] = self._collect_path(cli, merge_path(path, child_path), opt, stat_dict, stat_width)
            else:
                d[child_path] = None
        return d

    def post_validate(self, opt, arg):
        if len(arg) > 2:
            raise ValueError("'ls' only support one path")

    def _check_arg(self, arg):
        # kazoo会自动拼接上chroot
        if len(arg) == 1:
            # default current chroot path
            return '/'
        else:
            return arg[1]
