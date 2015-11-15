import tornado.web
import os
from url import handlers
import tornado.ioloop
import tornado.httpserver
import argparse

TEMPLATE_PATH = os.path.join(os.getcwd(),'static')
STATIC_PATH = os.path.join(os.getcwd(),'static')

class Application( tornado.web.Application ):

    def __init__(self):

        settings = dict(
                #template_path = TEMPLATE_PATH,
                static_path = STATIC_PATH,
            )

        tornado.web.Application.__init__(self,handlers,**settings)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='run config')
    parser.add_argument('--port',action='store',dest='port',type=int,default=8888)
    arguments = parser.parse_args()
    port = arguments.port
    app = Application()
    app = tornado.httpserver.HTTPServer(app)
    app.listen(port)
    tornado.ioloop.IOLoop.instance().start()
