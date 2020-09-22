from kazoo.client import KazooClient

import log


class Cli(object):

    def __init__(self, config=None):
        # TODO if chroot path not exists, this will occur exception
        self.config = config
        self.client = KazooClient(hosts=config.hosts)
        self.chroot = self.client.chroot if self.client.chroot else '/'

    def connect(self):
        if self.client:
            self.client.start()
            log.info('Zookeeper connected')

    def quit(self):
        if self.client:
            self.client.stop()

    @staticmethod
    def check_hosts(hosts):
        if '/' not in hosts:
            return hosts, None
        else:
            return hosts.split('/')
