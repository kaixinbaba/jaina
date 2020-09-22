from cmd.common import Command
from view.plain_ import PlainViewModel


class KaixinCommand(Command):
    """
    [green]This is for my dear daughter.[/green]

    [blue]Usage:
    \[jaina] kaixin[/blue]
    """

    confession = ':date:2017年10月2日，我的小宝贝:baby:诞生，爸爸爱你:kiss:!'

    def process(self, opt, arg, cli):
        return PlainViewModel(content=self.confession)
