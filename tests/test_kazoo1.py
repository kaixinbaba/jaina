from kazoo.client import KazooClient

client = KazooClient(hosts='127.0.0.1:2181')
try:
    client.start()
    r = client.delete('/jaina/adkfja/dfdf')
    print(r)
finally:
    client.stop()