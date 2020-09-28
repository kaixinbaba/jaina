from kazoo.client import KazooClient

client = KazooClient(hosts='127.0.0.1:2181')
try:
    client.start()
    r = client.get_acls('/test')
    print(r, type(r), len(r))
finally:
    client.stop()