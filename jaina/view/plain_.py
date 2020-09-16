from view.common import ViewHandler, ViewModel
import log


class PlainViewHandler(ViewHandler):

    def handle(self, view_model):
        log.log(view_model.content)


class PlainViewModel(ViewModel):

    def __init__(self, content):
        self.content = content

