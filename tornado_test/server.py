# coding=utf-8
import pymysql
import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop

from tornado.options import define,options
from tornado_test.urls import urls
from tornado_test import config

define('aport',default=8000,type=int,help='Port-8000')

class Application(tornado.web.Application):

    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.db = pymysql.Connection(
            **config.mysql
        )

def main():
    options.logging = config.log_level
    options.log_file_prefix = config.log_file
    tornado.options.parse_command_line()
    app = Application(
        urls, **config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.aport)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
