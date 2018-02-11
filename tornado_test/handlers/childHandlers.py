from tornado.web import RequestHandler
from . import baseHandler


class IndexHandler(RequestHandler):
    """首页"""

    def get(self, *args, **kwargs):
        pass