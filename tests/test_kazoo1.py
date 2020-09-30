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

    r = client.set_acls('/test', [make_acl('world', 'anyone', read=True, write=True, admin=True)])
    # r = client.get_acls('/test')
    print(r, type(r), len(r))
finally:
    client.stop()