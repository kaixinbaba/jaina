from view.common import ViewHandler, ViewModel
import log


class PlainViewHandler(ViewHandler):

    def handle(self, view_model):
        if view_model.color:
            getattr(log, view_model.color)(view_model.content)
        else:
            log.log(view_model.content)


class PlainViewModel(ViewModel):

    def __init__(self, content, color=None):
        self.content = content
        self.color = color

