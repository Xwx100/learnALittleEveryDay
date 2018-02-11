from tornado.web import RequestHandler


class Basehandler(RequestHandler):
    """childHandlers的基类"""

    def prepare(self):
        pass

    def write_error(self, status_code, **kwargs):
        pass

    def set_default_headers(self):
        pass

    def initialize(self):
        pass

    def on_finish(self):
        pass