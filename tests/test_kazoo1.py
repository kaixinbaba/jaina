from kazoo.client import KazooClient

client = KazooClient(hosts='127.0.0.1:2181/jaina')
try:
    client.start()
    r = client.create('/abc')
    print(r)
finally:
    client.stop()