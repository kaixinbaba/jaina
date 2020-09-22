import re

from exception import CommandNotExistsException
from manager import cmd_dict, view_dict


def handle_input(text, cli):
    tokens = re.split(r'\s+', text)
    first_token = tokens[0]
    if first_token.startswith("!"):
        # ! 开头的特殊处理下
        cmd = cmd_dict.get('!')
    else:
        # 优先从别名中查询
        full_cmd = cli.config.alias.get(first_token)
        if full_cmd:
            handle_input(full_cmd, cli)
            return
        else:
            cmd = cmd_dict.get(first_token)
            if cmd is None:
                raise CommandNotExistsException(f"The command '{first_token}' not exists!")
    # 命令解析用户输入，返回参数
    cmd_arg = cmd.parse_tokens(tokens)
    if not cmd_arg:
        # parse_args exception, just ignore
        return
    # 执行命令逻辑
    view_model = cmd.process(cmd_arg[0], cmd_arg[1], cli)
    if view_model:
        # 获取试图处理对象
        view = view_dict[view_model.name]
        # 处理返回的模型
        view.handle(view_model)
