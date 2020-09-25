from optparse import OptionParser

from cmd.common import Command
from util import merge_path


class CdCommand(Command):
    """
    [green]Change the 'chroot'.[/green]
    [white]Try '[bold]cd -h[/bold]' for more information about options.:smile:[/white]

    [blue]Example:
    (jaina) [/] cd /absolute/path
    (jaina) [/] cd relative/path
    (jaina) [/] cd ..
    (jaina) [/] cd ../..
    [/blue]
    """

    def __init__(self):
        self.parser = OptionParser()

    def process(self, opt, arg, cli):
        path = arg[1]
        old_chroot = cli.chroot
        if not path.startswith('/'):
            # TODO .. .
            # relative path
            new_path = self._get_relative_new_path(old_chroot, path)
        else:
            new_path = path
        cli.chroot = new_path
        if not cli.exists(''):
            # rollback
            cli.chroot = old_chroot
            raise ValueError(f"the path '{new_path}' not exists")

    def validate(self, tokens):
        if len(tokens) > 2:
            raise ValueError("cd only needs one 'path' parameter")
        if len(tokens) < 2:
            tokens.append('.')

    def _get_relative_new_path(self, old_chroot, path):
        path_split = path.split('/')
        chroot_split = old_chroot.split('/')
        # 弹出第一个空字符串
        chroot_split.pop(0)

        for p in path_split:
            if p == '..':
                if len(chroot_split) > 0:
                    chroot_split.pop()
            elif p == '.':
                continue
            else:
                chroot_split.append(p)
        print(chroot_split)
        new_path = merge_path('/', '/'.join(chroot_split))
        print(new_path)
        return new_path



