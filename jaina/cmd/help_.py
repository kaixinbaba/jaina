from optparse import OptionParser

from cmd.common import Command
from view.plain_ import PlainViewModel
from util import cmd


class HelpCommand(Command):
    """
    [green]Show all built-in command.[/green]

    [blue]Example:
    (jaina) \[/] help[/blue]
    (jaina) \[/] help <command>[/blue]
    """

    def __init__(self):
        self.parser = OptionParser()

    def process(self, opt, arg, cli):
        # FIXME lazy import
        from manager import cmd_dict
        if len(arg) == 1:
            # just help
            key_set = set(cmd_dict.keys())
            key_set.remove('kaixin')
            key_set.add('!<command>')
            all_cmd = '\n'.join(sorted(key_set))
            return PlainViewModel(content=f"[green]{all_cmd}[/green]\nTry to use 'help <command>' get more info.\n")
        else:
            cmd_str = arg[1]
            if cmd_str.startswith('!'):
                if cmd_str == '!':
                    content = cmd_dict['!'].__doc__
                else:
                    content = cmd('info ' + cmd_str[1:])
            else:
                if cmd_str not in cmd_dict:
                    raise ValueError(f'Can\'t find the \'{cmd_str}\' command')
                else:
                    content = cmd_dict[cmd_str].__doc__

            return PlainViewModel(content=content)

    def validate(self, tokens):
        if len(tokens) > 2:
            raise ValueError('The help command can only accept at most one <command>')
