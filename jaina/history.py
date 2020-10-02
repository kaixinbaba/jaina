import os

from config import jaina_home_path


class History(object):

    def __init__(self):
        self.history_file_path = os.path.join(jaina_home_path, 'history')
        if not os.path.exists(self.history_file_path):
            # init history file
            open(self.history_file_path, 'w').write('')

    def read_history(self, time=False):
        with open(self.history_file_path, 'r') as f:
            # return list(map(str.strip, f.readlines()[-limit:]))

            def _filter_line(line):
                line = line.strip()
                return (not line.startswith('#') if not time else True) and line

            result = []
            lines = list(map(str.strip, filter(_filter_line, f.readlines())))
            for i, line in enumerate(lines):
                if time:
                    if i % 2 == 1:
                        continue
                    else:
                        # # 2020-10-01 23:00:01.276349
                        time = line[2:21]
                        # 命令去掉最前面的+
                        content = f'[blue]{time}[/blue] {lines[i + 1][1:]}'
                        result.append(content)
                else:
                    result.append(line[1:])
            return result

