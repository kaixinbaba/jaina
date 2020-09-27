import os
import threading
from queue import Queue

from config import jaina_home_path


class FlushThreadThread(threading.Thread):

    def __init__(self, queue, history_file_path):
        threading.Thread.__init__(self, daemon=True)
        self.queue = queue
        self.history_file_path = history_file_path
        self.f = open(self.history_file_path, 'a')

    def run(self) -> None:
        while True:
            tokens = self.queue.get()
            self.f.write(tokens + '\n')
            self.f.flush()


class History(object):

    REAL_MAX_HISTORY = 1000

    def __init__(self, limit=1000):
        self.limit = limit
        self.history = Queue(maxsize=limit)
        self.history_file_path = os.path.join(jaina_home_path, 'history')
        self.flush_thread = FlushThreadThread(self.history, self.history_file_path)
        self.flush_thread.start()
        if not os.path.exists(self.history_file_path):
            # init history file
            open(self.history_file_path, 'w').write('')

    def append_history(self, tokens):
        self.history.put(tokens)

    def read_history(self, limit=500):
        with open(self.history_file_path, 'r') as f:
            return list(map(str.strip, f.readlines()[-limit:]))

    def shrink(self):
        history_list = self.read_history(History.REAL_MAX_HISTORY)
        if len(history_list) == History.REAL_MAX_HISTORY:
            # rewrite history to shrink file
            open(self.history_file_path, 'w').write('\n'.join(history_list))

