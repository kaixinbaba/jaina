from optparse import OptionParser

from kazoo.exceptions import NodeExistsError, NoNodeError

from cmd.common import Command
from view.plain_ import PlainViewModel


class CreateCommand(Command):
    """
    [green]Create a (persisent/ephemeral/sequential) node, default is permanent.[/green]
    [white]Try '[bold]create -h[/bold]' for more information about options.:smile:[/white]

    [blue]Example:
    \[jaina] create /test abc
    \[jaina] create -s /test
    \[jaina] create -s -e /test abc
    \[jaina] create -R /notExistsPath/test abc
    [/blue]
    """

    def __init__(self):
        self.parser = OptionParser()
        self.parser.add_option("-s", "--sequential",
                               action="store_true", dest="sequential", default=False,
                               help="Create sequential node")
        self.parser.add_option("-e", "--ephemeral",
                               action="store_true", dest="ephemeral", default=False,
                               help="Create ephemeral node")
        self.parser.add_option("-R", "--recursion",
                               action="store_true", dest="recursion", default=False,
                               help="Recursively create nodes even if the path does not exist")

    def process(self, opt, arg, cli):
        arg_len = len(arg)
        path = arg[1]
        data = arg[2] if arg_len > 2 else b''
        acl = arg[3] if arg_len > 3 else None
        try:
            return PlainViewModel(content=cli.client.create(path=path, value=data, acl=acl, ephemeral=opt.ephemeral,
                                                            sequence=opt.sequential, makepath=opt.recursion))
        except NoNodeError as e:
            raise ValueError(f"Path '{path}' not exists, try to add '-R' option")
        except NodeExistsError as e:
            raise ValueError(f"Path '{path}' already exists")

    def post_validate(self, opt, arg):
        # TODO check ACL arg
        arg_len = len(arg)
        if arg_len > 4:
            raise ValueError("'create' accepts up to 3 parameters (path, data, ACL)")
        if arg_len < 2:
            raise ValueError("'create' path is required")
