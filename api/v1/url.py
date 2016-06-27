from handlers import *
from verifyhandler import *

handlers = [
    (r'/api/v1/users/',UserHandler),
    (r'/api/v1/activity/list/',     ActivitiesHandler),
    (r'/api/v1/activity/add/',      ActivitiesHandler),
    (r'/api/v1/activity/deletion/', ActivityDetailHandler),
    (r'/api/v1/activity/attend/',   ActivityDetailHandler),
    (r'/api/v1/activity/finish/',   ActivityAttendHandler),
    (r'/api/v1/activity/people/',   ActivityAttendHandler),
    (r'/api/v1/activity/complete/',ActivityFinishHandler),
    (r'/api/v1/activity/joined/',   UserAttendHandler),
    (r'/api/v1/activity/published/',UserHostHandler),
    (r'/api/v1/verify/',            LeanCloudVerifyHandler),
    (r'/api/v1/city/',              CityHandler),
    (r'/api/v1/splash/',            SplashHandler),
    (r'/api/v1/user/detail/(?P<uid>[a-zA-Z0-9\-]+)/',UserDetailHandler),
    (r'/api/v1/threepart/',OAuthorHandler),
    (r'/.*',NotFoundHandler),
]
