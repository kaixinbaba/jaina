from optparse import OptionParser

from cmd.common import Command


class SetAclCommand(Command):
    """
    [green]Set permission information of the specified path.[/green]
    [white]Try '[bold]setAcl -h[/bold]' for more information about options.:smile:[/white]
    [yellow]
    scheme: world | ip | digest | super
    type:
        when scheme == 'world'  >> 'anynone'
        when scheme == 'ip'     >> 'some ip address'
        when scheme == 'digest' >> 'username:base64password'
        when scheme == 'super'  >> like 'digest'
    perm:
        c   : Create
        d   : Delete
        r   : Read
        w   : Write
        a   : Admin
        all : All above
    [/yellow]
    [blue]Example:
    (jaina) \[/] setAcl /your/path scheme:type:perm
    (jaina) \[/] setAcl -v 1 /your/path scheme:type:perm
    (jaina) \[/] setAcl /your/path world:anyone:cdrwa
    (jaina) \[/] setAcl /your/path ip:192.168.1.11:cwa
    (jaina) \[/] setAcl /your/path ip:192.168.1.11/24:cd
    (jaina) \[/] setAcl /your/path digest:<username>:<base64password>:r
    [/blue]
    """

    def __init__(self, name):
        super().__init__(name)
        self.parser = OptionParser()
        self.parser.add_option("-v", "--version",
                               action="store", type=int, dest="version", default=-1,
                               help="Version requirements of the target node, any if -1, default -1")

    def process(self, opt, arg, cli):
        print(opt, arg)
