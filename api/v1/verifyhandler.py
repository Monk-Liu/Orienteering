from handlers import BaseHandler,JSONHandler
from tornado import gen,httpclient
from config import GEETEST,LEANCLOUD
from hashlib import md5 
from tornado.httputil import HTTPHeaders
import tornado.web
import json
from database import User,UserInfo

class GeetestVerifyHandler(BaseHandler):
    
    #tornado gen 异步的问题
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

            http_request =  httpclient.HTTPRequest(GEETEST["API_SERVER"],method="POST",body=query)
            http_cli = httpclient.AsyncHTTPClient()
            response = yield  http_cli.fetch(request=http_request)
            #print(response,'\n',dir(response))
            backinfo = response.body
            if isinstance(backinfo,bytes):
                backinfo = backinfo.decode()
            #if backinfo == self.md5value(seccode):
                #self.write("success")
            #else:
                #self.write("fail")
            return backinfo



    def md5value(self,pre_value):
        m = md5()
        if not isinstance(pre_value,bytes): 
            pre_value = pre_value.encode()
        m.update(pre_value)
        return m.hexdigest()

    
    def get(self):
        self.gt_register()

    @gen.coroutine
    def post(self):
        challenge = self.get_argument('geetest_challenge')
        validate = self.get_argument('geetest_validate')
        seccode = self.get_argument("geetest_seccode")
        res =  yield self.gt_validate(challenge,validate,seccode)
        if res == self.md5value(seccode):
            self.write('success')
        else:
            self.write('fail')
    

class LeanCloudVerifyHandler(JSONHandler):

    @gen.coroutine
    def sendSMS(self,phone):
        data = json.dumps({"mobilePhoneNumber":phone})
        headers = HTTPHeaders()
        headers.add("Content-Type",'application/json')
        headers.add("X-LC-Id",LEANCLOUD["ID"])
        headers.add("X-LC-Key",LEANCLOUD["KEY"])
        req = httpclient.HTTPRequest(LEANCLOUD["SURL"],method="POST",body=data,
                                    headers=headers)
        http_cli = httpclient.AsyncHTTPClient()
        response = yield http_cli.fetch(req,raise_error=False)
        if response.body:
            print("SendSMS to %s"%phone)
            return json.loads(response.body.decode())
        else:
            print("SendSMS no respone")
            return 1

    @gen.coroutine
    def get(self):
        phone = self.get_argument("phone",'')
        if not phone:
            return
        res = yield self.sendSMS(phone)
        print(res)
        if res:
            error = res['error'] if 'error' in res else "fail"
            self.write_error(error)
        else:
            self.write_success()

    @gen.coroutine
    def verifySMS(self,code,phone):
        url = LEANCLOUD['VURL']%(code,phone)
        print(url)
        data = json.dumps({"code":code,"mobilePhoneNumber":phone}) # why body can't be None?
        headers = HTTPHeaders()
        headers.add("Content-Type",'application/json')
        headers.add("X-LC-Id",LEANCLOUD["ID"])
        headers.add("X-LC-Key",LEANCLOUD["KEY"])
        req = httpclient.HTTPRequest(url,method="POST",body=data,headers=headers)
        http_cli = httpclient.AsyncHTTPClient()
        response = yield http_cli.fetch(req,raise_error=False)

        if response.body:
            return json.loads(response.body.decode())
        else:
            return 1

    @gen.coroutine
    def post(self):
        phone = self.json_args['phone'] 
        code = self.json_args['code']
        password = self.json_args['password']
        res = yield self.verifySMS(code,phone)
        if not res:
            user = User(phone,password)
            info = UserInfo()
            user.info.append(info)
            self.session.add(user)
            self.session.commit()
            self.write_success()
        else:
            error = res['error'] if 'error' in res else "fail"
            self.write_error(error)
