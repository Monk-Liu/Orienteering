from handlers import *

handlers = [
    (r'/',LoginHandler),
    (r'/login/',LoginHandler),
    (r'/show/users/', ShowUserHandler),
    (r'/show/events/',ShowEventHandler),
    (r'/show/users/relation/', UserByEventHandler),
    (r'/show/events/relation/', EventByUserHandler),
    (r'/show/activity/check/', ActivityCheckHandler),
    (r'/show/team/detail/', ActivityTeamHandler),#显示队伍信息
    #(r'/show/activity/team/running/', ActivityRunHandler),
    (r'/show/points/', ActivityPointHandler),
    (r'/change/disclaimer/', DisclaimerHandler)
]
