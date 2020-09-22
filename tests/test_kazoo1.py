from kazoo.client import KazooClient

client = KazooClient(hosts='127.0.0.1:2181')
try:
    client.start()
    r = client.exists('/test')
    print(r)
finally:
    client.stop()