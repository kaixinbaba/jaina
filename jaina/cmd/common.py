from abc import abstractmethod, ABCMeta

import log


class CommandArgument(metaclass=ABCMeta):
    pass


class Command(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    def parse_tokens(self, tokens):
        self.validate(tokens)
        try:
            if hasattr(self, 'parser'):
                opt, arg = self.parser.parse_args(tokens)
                self.post_validate(opt, arg)
                return opt, arg
            else:
                return None, tokens
        except SystemExit as se:
            # prevent exit
            pass

    def validate(self, tokens):
        pass

    def post_validate(self, opt, arg):
        pass

    @abstractmethod
    def process(self, opt, arg, cli):
        pass

    def alias_list(self):
        pass


def default_watch(r):
    log.info(r)
