import tornado.web
from tornado import gen
from tornado import httpclient
import json
import database as DB
from config import GEETEST
from hashlib import md5


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
    
    def get(self):
        self.write('sss')
    


class UserDetailHandler(JSONHandler):

    pass


class ActivityHandler(JSONHandler):

    pass


class ActivityDetailHandler(JSONHandler):
    
    pass


class VerifyHandler(BaseHandler):
    

    #调用极验接口
    @tornado.web.asynchronous
    def gt_register(self):
        apireg = GEETEST['REGISTER_URL']
        regurl = apireg + "gt=%s"%GEETEST['CAPTCHA_ID']
        http_cli = httpclient.AsyncHTTPClient()
        try:
            http_cli.fetch(regurl,callback=self.on_response)
        except httpclient.HTTPError as e:
            print("Error:%s",str(e))
    
    def on_response(self,response):
        challenge = response.body
        if isinstance(challenge,bytes):
            challenge = challenge.decode()
        if len(challenge) == 32:
            url = "%s%s&challenge=%s&product=%s" %(GEETEST['BASE_URL'],
                                                  GEETEST['CAPTCHA_ID'],
                                                  challenge,
                                                  GEETEST['PRODUCT'])
            self.render('geetest.html',url=url)
        else:
            self.write('fail')


    @gen.coroutine
    def gt_validate(self,challenge,validate,seccode):
        if validate == self.md5value(GEETEST["PRIVATE_KEY"]+"geetest"+challenge):
            query = 'seccode='+seccode+"&sdk=python_"+GEETEST['PY_VERSION']

            http_request = httpclient.HTTPRequest(GEETEST["API_SERVER"],method="POST",body=query)
            http_cli = httpclient.AsyncHTTPClient()
            response = yield http_cli.fetch(request=http_request)
            print(response,'\n',dir(response))
            backinfo = response.body
            print('backinfo is',backinfo)
            return backinfo


    def md5value(self,pre_value):
        m = md5()
        if not isinstance(pre_value,bytes): 
            pre_value = pre_value.encode()
        m.update(pre_value)
        return m.hexdigest()

    
    def get(self):
        self.gt_register()

    def post(self):
        challenge = self.get_argument('geetest_challenge')
        validate = self.get_argument('geetest_validate')
        seccode = self.get_argument("geetest_seccode")
        res = self.gt_validate(challenge,validate,seccode)
        print(res)
        if res == self.md5value(seccode):
            self.write('success')
        else:
            self.write('fail')
