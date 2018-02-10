# coding=utf-8

import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop

from tornado.options import define,options

define('aport',default=8000,type=int,help='Port-8000')

class indexhandler(tornado.web.RequestHandler):
    # def get(self, *args, **kwargs):
    #     self.write('您好啊')
    pass

def main():
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [(r'/',indexhandler),]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.aport)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
