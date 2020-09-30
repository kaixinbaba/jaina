from optparse import OptionParser

from kazoo.exceptions import NoNodeError, NoAuthError

from cmd.acl_util import int2perm
from cmd.common import Command
from util import get_stat_content
from view.plain_ import PlainViewModel


class GetAclCommand(Command):
    """
    [green]Get permission information of the specified path.[/green]
    [white]Try '[bold]getAcl -h[/bold]' for more information about options.:smile:[/white]

    [blue]Example:
    (jaina) \[/] getAcl /your/path
    (jaina) \[/] getAcl -s /need/stat/path
    [/blue]
    """

    def __init__(self, name):
        super().__init__(name)
        self.parser = OptionParser()
        self.parser.add_option("-s", "--stat",
                               action="store_true", dest="stat", default=False,
                               help="Also show the path statistics info, default False")

    def post_validate(self, opt, arg):
        if len(arg) < 2:
            raise ValueError("getAcl path is required")

    def process(self, opt, arg, cli):
        path = arg[1]
        try:
            acl_list, stat = cli.client.get_acls(path)
            acl = acl_list[0]
            c = [f'{acl.id.scheme}:{acl.id.id}', f'[blue]{int2perm(acl.perms)}[/blue]']
            if opt.stat:
                c.append('-'*10)
                c.append(get_stat_content(stat))
            return PlainViewModel(content='\n'.join(c), color='info')
        except NoAuthError as e:
            raise ValueError(f"Authentication is not valid, '{path}'")
        except NoNodeError as e:
            raise ValueError(f"Path '{path}' not exists")
