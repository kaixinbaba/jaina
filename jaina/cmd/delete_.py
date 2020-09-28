from optparse import OptionParser

from kazoo.exceptions import NotEmptyError, NoNodeError

from cmd.common import Command
from view.plain_ import PlainViewModel


class DeleteCommand(Command):
    """
    [green]Delete a node.[/green]
    [white]Try '[bold]delete -h[/bold]' for more information about options.:smile:[/white]

    [blue]Example:
    (jaina) \[/] delete /leaf
    (jaina) \[/] delete -v 1 /leaf
    (jaina) \[/] delete -R /very/deep/path
    [/blue]
    """

    def __init__(self, name):
        super().__init__(name)
        self.parser = OptionParser()
        self.parser.add_option("-v", "--version",
                               action="store", type=int, dest="version", default=-1,
                               help="Version requirements of the target node, any if -1, default -1")
        self.parser.add_option("-R", "--recursion",
                               action="store_true", dest="recursion", default=False,
                               help="Recursively delete node and all its children, same as 'deleteall' in zkCli, default False")

    def process(self, opt, arg, cli):
        try:
            cli.client.delete(arg[1], version=opt.version, recursive=opt.recursion)
            return PlainViewModel(content=f'[green]successfully deleted[/green]')
        except NoNodeError as e:
            raise ValueError(f"The path '{arg[1]}' not exists")
        except NotEmptyError as e:
            raise ValueError("Can't delete un-leaf node without '-R' option")

    def post_validate(self, opt, arg):
        if len(arg) != 2:
            raise ValueError('delete path is required')




