from collections import defaultdict
from optparse import OptionParser

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
                               version,cversion,aversion,mtime,numChildren
                               """)
        self.parser.add_option("-w", "--watch",
                               action="store_true", dest="watch", default=False,
                               help="Add watch to the path")
        self.parser.add_option("-R", "--recursion",
                               action="store_true", dest="recursion", default=False,
                               help="Recursively display all nodes under the path, "
                                    "conflict with '-s', priority is higher than -s")
        self.stat_width_fields = ['version', 'cversion', 'aversion', 'numChildren']

    def process(self, cmd_arg, cli):
        if not cmd_arg:
            # parse_args exception, just ignore
            return
        opt, arg = cmd_arg
        path = self._check_arg(arg, chroot=cli.chroot)
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
        r = cli.client.get_children(path, default_watch if opt.watch else None, opt.stat)
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

    def parse_tokens(self, tokens):
        try:
            return self.parser.parse_args(tokens)
        except SystemExit as se:
            # prevent exit
            pass

    def _check_arg(self, arg, chroot='/'):
        if len(arg) > 2:
            raise ValueError("'ls' only support one path")
        if len(arg) == 1:
            # default current chroot path
            return chroot
        else:
            return merge_path(chroot, arg[1])
