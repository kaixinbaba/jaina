from optparse import OptionParser

from cmd.common import Command
from util import get_relative_new_path


class CdCommand(Command):
    """
    [green]Change the 'chroot'.[/green]
    [white]Try '[bold]cd -h[/bold]' for more information about options.:smile:[/white]

    [blue]Example:
    (jaina) \[/] cd /absolute/path
    (jaina) \[/] cd relative/path
    (jaina) \[/] cd ..
    (jaina) \[/] cd ../..
    [/blue]
    """

    def __init__(self, name):
        super().__init__(name)
        self.parser = OptionParser()

    def process(self, opt, arg, cli):
        path = arg[1]
        old_chroot = cli.chroot
        if not path.startswith('/'):
            # relative path
            new_path = get_relative_new_path(old_chroot, path)
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
