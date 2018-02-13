from tornado_test.handlers import childHandlers


urls = [
    (r'/',childHandlers.IndexHandler),
]
