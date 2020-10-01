from kazoo.client import KazooClient
from kazoo.security import ACL, make_acl

client = KazooClient(hosts='127.0.0.1:2181')
try:
    client.start()
    # world auth digest ip
    scheme = ''
    # anyone
    # addauth digest user:pwd
    # username:base64
    #
    ID = ''
    r = client.add_auth('digest', 'xjj:123456')
    # print(r, type(r))
    r = client.set_acls('/a', [make_acl('auth', '', all=True)])
    # r = client.get_acls('/a')
    print(r, type(r), len(r))
finally:
    client.stop()