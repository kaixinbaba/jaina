from cmd.common import Command


class QuitCommand(Command):

    def process(self, opt, arg, cli):
        raise KeyboardInterrupt
