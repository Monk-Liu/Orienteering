import tornado.web
import json
import database as DB


class BaseHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.session = DB.Session()
        self.redis = DB.Redis()

    def on_finish(self):
        self.session.close()


class JSONHandler(BaseHandler):

    def set_default_headers(self):
        self.set_header("Content-Type","application/json;charset=UTF-8")

    def prepare(self):
        self.res ={}
        if self.request.method not in ("GET","HEAD"):
            try:
                body = self.request.body.decode('utf8')
                if body:
                    self.json_args = json.loads(body)
                else:
                    self.json_args = None
            except Exception as e:
                print("json arguments error")

    def write_error(self,mesg):
        self.res['status'] = 2
        self.res['mesg'] = mesg

        self.finish(json.dumps(self.res))

class UserHandler(JSONHandler):

    pass


class UserDetailHandler(JSONHandler):

    pass


class ActivityHandler(JSONHandler):

    pass


class ActivityDetailHandler(JSONHandler):
    
    pass


class VerifyHandler(JSONHandler):

    pass
