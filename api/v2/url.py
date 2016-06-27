from handlers import *
from verifyhandler import *

handlers = [
    (r'/api/v2/users/',UserHandler),
    (r'/api/v2/activity/list/',     ActivitiesHandler),
    (r'/api/v2/activity/add/',      ActivitiesHandler),
    (r'/api/v2/activity/deletion/', ActivityDetailHandler),
    (r'/api/v2/activity/attend/',   ActivityDetailHandler),#报名
    (r'/api/v2/activity/finish/',   ActivityAttendHandler),#报名
    (r'/api/v2/activity/people/',   ActivityAttendHandler),#参加活动的人/队伍
    (r'/api/v2/activity/complete/',ActivityFinishHandler),#完成
    (r'/api/v2/activity/joined/',   UserAttendHandler),#参加的活动哦你
    (r'/api/v2/activity/published/',UserHostHandler),#发起的活动
    (r'/api/v2/activity/team/', TeamHandler), #type=0,创建团队; type=1, 队员加入团队 #get 取消报名
    (r'/api/v2/activity/member/', MemberHandler),
    (r'/api/v2/activity/team/detail/',TeamDetailHandler),
    (r'/api/v2/activity/running/(?P<activity_id>[a-zA-Z0-9\-]+)/',RealTimeHandler), #比赛中
    (r'/api/v2/activity/check/', CheckHandler),
    (r'/api/v2/activity/run/', RunningHandler),
    (r'/api/v2/activity/point/', PointArriveHandler), #完成一个点 点的id， 
    (r'/api/v2/activity/team/finish/',FinishTeamHandler),
    (r'/api/v2/activity/rank/', RankListHandler), 
    (r'/api/v2/verify/',            LeanCloudVerifyHandler),
    (r'/api/v2/city/',              CityHandler),
    (r'/api/v2/splash/',            SplashHandler),
    (r'/api/v2/disclaimer/',    DisclaimerHandler),
    (r'/api/v2/user/detail/(?P<uid>[a-zA-Z0-9\-]+)/',UserDetailHandler),
    (r'/api/v2/threepart/',OAuthorHandler),
    (r'/.*',NotFoundHandler),
]
