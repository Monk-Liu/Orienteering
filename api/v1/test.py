import json 
from tornado import httpclient 
from tornado.httputil import HTTPHeaders
from config import LEANCLOUD
from tornado import gen

@gen.coroutine
def sendSMS(phone):
        data = json.dumps({"mobilePhoneNumber":phone})
        headers = HTTPHeaders()
        headers.add("Content-Type",'application/json')
        headers.add("X-LC-Id",LEANCLOUD["ID"])
        headers.add("X-LC-Key",LEANCLOUD["KEY"])
        req = httpclient.HTTPRequest(LEANCLOUD["SURL"],method="POST",body=data,
                                    headers=headers)
        http_cli = httpclient.HTTPClient()
        response = http_cli.fetch(req)
        print(response.body)
        if response:
            return response.body
            print("SendSMS to %s"%phone)
        else:
            print("SendSMS no respone")


if __name__ == "__main__":
    sendSMS('15927278893')
