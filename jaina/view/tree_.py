import time

import log
from util import merge_path
from view.common import ViewHandler, ViewModel, green, blue, purple, white


class TreeViewHandler(ViewHandler):
    start = '|'
    line = '--'

    def handle(self, view_model):
        content = []
        self._complete_content(view_model.tree_dict, content, view_model.stat_dict, view_model.stat_width, 0)
        log.log('\n'.join(content))

    def _complete_content(self, tree_dict, content, stat_dict, stat_width, level, parent_path=None):
        for index, (path, childs) in enumerate(tree_dict.items()):
            full_current_path = merge_path(parent_path, path)
            content.append(self._append_str(path, level, stat_dict.get(full_current_path), stat_width, parent_path))
            if childs:
                self._complete_content(childs, content, stat_dict, stat_width, level + 1, parent_path=full_current_path)

    def _append_str(self, path, level, stat, stat_width, parent_path):
        s = []
        if stat is not None:
            s.append(self._with_stat(stat, stat_width))
        if level > 0 and parent_path != '/':
            s.append('   ' * level)
        if level > 0:
            s.append(self.start)
            s.append(self.line)
        if stat and stat.numChildren > 0:
            s.append(green(path))
        else:
            s.append(path)
        return ''.join(s)

    def _with_width_stat(self, stat, field, stat_width):
        value = getattr(stat, field)
        width = stat_width[field]
        return str(value).ljust(width, ' ')

    def _with_stat(self, stat, stat_width):
        temp = []
        temp.append(green(f'v:{self._with_width_stat(stat, "version", stat_width)} '))
        temp.append(green(f'c:{self._with_width_stat(stat, "cversion", stat_width)} '))
        temp.append(green(f'a:{self._with_width_stat(stat, "aversion", stat_width)} '))
        temp.append(blue(f' {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stat.mtime / 1000))} '))
        if stat.numChildren > 0:
            temp.append(purple(f'\[{self._with_width_stat(stat, "numChildren", stat_width)}] '))
        else:
            temp.append(white(f'\[{self._with_width_stat(stat, "numChildren", stat_width)}] '))
        return ''.join(temp)


class TreeViewModel(ViewModel):

    def __init__(self, root_path, tree_dict, stat_dict, stat_width):
        self.root_path = root_path
        self.tree_dict = tree_dict
        self.stat_dict = stat_dict
        self.stat_width = stat_width
