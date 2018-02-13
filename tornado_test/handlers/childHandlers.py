from tornado_test.handlers import baseHandler


class IndexHandler(baseHandler.Basehandler):
    """首页"""

    def get(self, *args, **kwargs):
        self.write('hello,许伟新')