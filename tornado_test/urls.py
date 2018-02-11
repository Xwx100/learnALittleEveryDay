from .handlers import childHandlers


urls = [
    (r'/',childHandlers.IndexHandler),
]
