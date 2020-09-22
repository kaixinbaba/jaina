from kazoo.client import KazooClient

import log


class Cli(object):

    def __init__(self, config=None):
        # TODO if chroot path not exists, this will occur exception
        self.config = config
        self.client = KazooClient(hosts=config.hosts)
        self._chroot = self.client.chroot if self.client.chroot else '/'
        self._abs_chroot = self._chroot

    def connect(self):
        if self.client:
            self.client.start()
            log.info('Zookeeper connected')

    def quit(self):
        if self.client:
            self.client.stop()

    def exists(self, path):
        try:
            return self.client.exists(path) is not None
        except Exception as e:
            return False

    @staticmethod
    def check_hosts(hosts):
        if '/' not in hosts:
            return hosts, None
        else:
            return hosts.split('/')

    @property
    def chroot(self):
        return self._chroot

    @chroot.setter
    def chroot(self, chroot):
        self._chroot = chroot
        self.client.chroot = chroot
