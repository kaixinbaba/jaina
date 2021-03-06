from optparse import OptionParser

from kazoo.exceptions import NoAuthError, NoNodeError
from kazoo.security import make_acl, make_digest_acl_credential

from cmd.acl_util import validate_scheme, validate_perm, validate_id, schemes
from cmd.common import Command
from view.plain_ import PlainViewModel


class SetAclCommand(Command):
    """
    [green]Set permission information of the specified path.[/green]
    [white]Try '[bold]setAcl -h[/bold]' for more information about options.:smile:[/white]
    [yellow]
    scheme: world | ip | digest | super
    type:
        when scheme == 'world'  >> 'anynone'
        when scheme == 'ip'     >> 'some ip address'
        when scheme == 'digest' >> 'username:BASE64(SHA1(username:password))'
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
        self.parser.add_option("-u", "--unencrypted",
                               action="store_true", dest="unencrypted", default=False,
                               help="""Use the original password when setting the digest.
                               There is a program that automatically performs base64 encryption.
                               This parameter takes effect only when the scheme is equal to 'digest'.
                               The default is False""")

    def post_validate(self, opt, arg):
        if len(arg) != 3:
            raise ValueError("setAcl 'path' and 'perm' is required!")
        acl_info = arg[2].split(':')
        if len(acl_info) == 4:
            scheme, username, password, perm = acl_info
            id = f'{username}:{password}'
        elif len(acl_info) == 3:
            scheme, id, perm = acl_info
        else:
            raise ValueError("Illegal permission format, please input 'help setAcl' to get more info")
        scheme = scheme.lower()
        perm = perm.lower()

        if not validate_scheme(scheme):
            raise ValueError(f"scheme is not valid, must in {schemes}, but got '{scheme}'")

        if not validate_perm(perm):
            raise ValueError(
                f"perm is not valid, can only be a combination of these characters('c', 'd', 'r', 'w', 'a'), "
                f"or 'all', but got '{perm}'")
        if not validate_id(scheme, id):
            raise ValueError(f"id's format is not valid scheme '{scheme}' got '{id}'")

    def process(self, opt, arg, cli):
        path = arg[1]

        # FIXME duplicate code
        acl_info = arg[2].split(':')
        if len(acl_info) == 4:
            scheme, username, password, perm = acl_info
            id = f'{username}:{password}'
        elif len(acl_info) == 3:
            scheme, id, perm = acl_info
        scheme = scheme.lower()
        perm = perm.lower()
        if opt.unencrypted and scheme == 'digest':
            username, password = id.split(":")
            id = make_digest_acl_credential(username, password)

        try:
            perm_kw = {
                'all': perm == 'all',
                'read': 'r' in perm,
                'write': 'w' in perm,
                'create': 'c' in perm,
                'delete': 'd' in perm,
                'admin': 'a' in perm,

            }
            cli.client.set_acls(path,
                                [make_acl(scheme, id, **perm_kw)],
                                opt.version)
        except NoAuthError as e:
            raise ValueError(f"Authentication is not valid, '{path}'")
        except NoNodeError as e:
            raise ValueError(f"Path '{path}' not exists")
        except Exception as e:
            import traceback
            raise ValueError(f"Illegal arguments! {traceback.format_exc()}")
        return PlainViewModel(content='setAcl successfully', color='info')
