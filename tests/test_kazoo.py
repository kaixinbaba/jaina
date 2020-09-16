import unittest
from kazoo.client import KazooClient



class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.client = KazooClient(hosts='127.0.0.1:2181/jaina')
        self.client.start()
        # self.client.create('/jaina')
        # self.client.chroot = '/jaina'

    def test_create(self):
        self.client.create('test', 'abc'.encode())

    def test_delete(self):
        self.client.delete('/test')

    def test_get(self):
        value = self.client.get('/test')
        print(value[0], type(value[0]))
        print(value[0].decode())
        print(value[1], type(value[1]))

    def tearDown(self) -> None:
        self.client.stop()


if __name__ == '__main__':
    unittest.main()