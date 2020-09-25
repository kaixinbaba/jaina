from optparse import OptionParser

from cmd.common import Command
from config import write_config
from view.plain_ import PlainViewModel


class AliasCommand(Command):
    """
    [green]Set or query alias.[/green]
    [white]Try '[bold]alias -h[/bold]' for more information about options.:smile:[/white]

    [blue]Example:
    (jaina) [/] alias
    (jaina) [/] alias <alias>
    (jaina) [/] alias <alias> '<cmd> [arg] (options)'
    [/blue]
    """

    def __init__(self):
        self.parser = OptionParser()

    def process(self, opt, arg, cli):
        arg_len = len(arg)
        if arg_len == 1:
            # 查询所有的alias
            content = self._query_all_alias(cli.config)
        elif arg_len == 2:
            # 查询指定alias
            content = self._query_specify_alias(cli.config, arg[1])
        else:
            # 设置alias
            content = self._set_specify_alias(cli.config, arg)
        return PlainViewModel(content=content)

    def _query_all_alias(self, config):
        if hasattr(config, 'alias'):
            return '[green]' + '\n'.join([f"{k}='[red]{v}[/red]'" for k, v in config.alias.items()]) + '[/green]'
        else:
            return ''

    def _query_specify_alias(self, config, alias_name):
        if hasattr(config, 'alias'):
            if alias_name not in config.alias:
                return ''
            return f'[green]{config.alias[alias_name]}[/green]'
        else:
            return ''

    def _set_specify_alias(self, config, arg):
        # 设置alias
        arg.pop(0)
        alias_name = arg.pop(0)
        # 去除引号
        full_cmd = ' '.join(map(lambda x: x.replace("'", '').replace('"', ''), arg))
        old_alias = config.get('alias')
        old_alias[alias_name] = full_cmd
        config.set('alias', old_alias)
        write_config(config)
        return f"[green]alias {alias_name}='[red]{full_cmd}[/red]' updated[/green]"
