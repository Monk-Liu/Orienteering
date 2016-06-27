import tornado.web
import os
from url import handlers
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port",default=8888,type=int,help="Server port")

TEMPLATE_PATH = os.path.join(os.getcwd(),'templates')
STATIC_PATH = os.path.join(os.getcwd(),'static')

class Application( tornado.web.Application ):

    def __init__(self):

        settings = dict(
                template_path = TEMPLATE_PATH,
                static_path = STATIC_PATH,
            )

        tornado.web.Application.__init__(self,handlers,**settings)

if __name__ == "__main__":
    #parser = argparse.ArgumentParser(description='run config')
    #parser.add_argument('--port',action='store',dest='port',type=int,default=8888)
    #arguments = parser.parse_args()
    tornado.options.parse_command_line()
    port = options.port
    app = Application()
    try:
        server = tornado.httpserver.HTTPServer(app,xheaders=True)
        server.bind(port)
        server.start(2)
        tornado.ioloop.IOLoop.instance().start()
    except OSError:
        pass
    except Exception as e:
        print(str(e))
