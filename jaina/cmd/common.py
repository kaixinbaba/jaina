from abc import abstractmethod, ABCMeta

import log


class CommandArgument(metaclass=ABCMeta):
    pass


class Command(metaclass=ABCMeta):

    def parse_tokens(self, tokens):
        self.validate(tokens)
        try:
            opt, arg = self.parser.parse_args(tokens)
            self.post_validate(opt, arg)
            return opt, arg
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


def default_watch(r):
    log.info(r)
