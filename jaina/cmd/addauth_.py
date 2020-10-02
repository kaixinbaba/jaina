from optparse import OptionParser

from cmd.common import Command
from view.plain_ import PlainViewModel


class AddAuthCommand(Command):
    """
    [green]Set permission information of the specified path, default only support 'digest'.[/green]
    [white]Try '[bold]addauth -h[/bold]' for more information about options.:smile:[/white]
    alias: login

    [blue]Example:
    (jaina) \[/] addauth username password
    (jaina) \[/] addauth username:password
    [/blue]
    """

    def __init__(self, name):
        super().__init__(name)
        self.parser = OptionParser()

    def post_validate(self, opt, arg):
        if len(arg) < 3:
            if len(arg) == 2:
                if len(arg[1].split(':')) != 2:
                    raise ValueError("Please check the correct format 'username:password' in 'digest' mode")
            else:
                raise ValueError("'username' and 'password' is required in 'digest' mode")

    def process(self, opt, arg, cli):
        if len(arg) >= 3:
            credential = f'{arg[1]}:{arg[2]}'
        else:
            credential = arg[1]
        try:
            cli.client.add_auth('digest', credential)
        except Exception as e:
            raise ValueError(f"addauth occur error, {e}")
        else:
            return PlainViewModel(content='addauth successfully', color='info')

    def alias_list(self):
        return ['login']
