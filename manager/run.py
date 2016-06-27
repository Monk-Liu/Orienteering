import tornado.web
import os
from url import handlers
import tornado.ioloop
import tornado.httpserver
import argparse


TEMPLATE_PATH = os.path.join(os.path.dirname(__file__),'templates')
STATIC_PATH = os.path.join(os.path.dirname(__file__),'static')
#TEMPLATE_PATH = '/root/Qudong/manager/templates/'
#STATIC_PATH = '/root/Qudong/manager/static/'

class Application( tornado.web.Application ):

    def __init__(self):
        settings = dict(
                template_path = TEMPLATE_PATH,
                static_path = STATIC_PATH,
                cookie_secret = "qudong",
                login_url = "/login/",
            )

        tornado.web.Application.__init__(self,handlers,**settings)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='run config')
    parser.add_argument('--port',action='store',dest='port',type=int,default=8008)
    arguments = parser.parse_args()
    port = arguments.port
    app = Application()
    try:
        server = tornado.httpserver.HTTPServer(app,xheaders=True)
        server.bind(port)
        server.start()
        tornado.ioloop.IOLoop.instance().start()
    except OSError:
        pass
    except Exception as e:
        print(str(e))
