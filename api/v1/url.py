from handlers import *
from verifyhandler import *

handlers = [
    (r'/api/v1/users/',UserHandler),
    (r'/api/v1/activities/',ActivityHandler),
    (r'/api/v1/activity/detail/(?P<uid>[a-zA-Z0-9\-]+)',ActivityDetailHandler),
    (r'/api/v1/user/detail/(?P<uid>[a-zA-Z0-9\-]+)',UserDetailHandler),
    #(r'/api/v1/verify/',VerifyHandler),
    (r'/api/v1/leancloud/verify/',LeanCloudVerifyHandler),
]
