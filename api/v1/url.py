from handlers import *
from verifyhandler import *

handlers = [
    (r'/api/v1/users/',UserHandler),
    (r'/api/v1/activities/',ActivitiesHandler),
    (r'/api/v1/activity/',ActivityDetailHandler),
    (r'/api/v1/user/detail/(?P<uid>[a-zA-Z0-9\-]+)',UserDetailHandler),
    #(r'/api/v1/verify/',VerifyHandler),
    (r'/api/v1/verify/',LeanCloudVerifyHandler),
    (r'/api/v1/city/',CityHandler),
    (r'/api/v1/splash/',SplashHandler),
]
