from abc import abstractmethod, ABCMeta


class CommandArgument(metaclass=ABCMeta):
    pass


class Command(metaclass=ABCMeta):

    @abstractmethod
    def parse_tokens(self, tokens):
        pass

    @abstractmethod
    def process(self, cmd_arg, cli):
        pass
