###创建团队
/api/v2/activity/add/
#####request
+ type: 1表示个人， 0表示团体
+ key:
+ name:
+ apply_start:
+ appley_end:
+ game_start:
+ game_end:
+ description:
+ loc_x:
+ loc_y:
+ loc_road:
+ loc_province:
+ loc_city:
+ loc_province:
+ loc_distract:
+ person_limit: int
+ person_per_team: int
+ prize:
+ spotlist:[{}...]
  {"x":111,"y":111,"radius":100,"type":1,//返回的时候会有id:1}

#####response
+ event: 0 表示成功
+ message
+ data


###报名(团体赛)(POST)
/api/v2/activity/team/
#####request
+ type: 0表示我是队长， 1表示我是队员
+ activity_id
+ key：(用户key)
+ name
+ slogan
+ urgent_phone
+ urgent_contact
+ members [{},{}] -> name, idcard, phone, sex
#####response
+ event
+ message
+ data:{}


###取消报名(GET)
/api/v2/activity/team/
#####request
+ team_id
+ activity_id
#####response
+ event
+ message
+ data

###完成一个点
/api/v2/activity/point/
#####request
+ team_id
+ point_id
+ finish_time
#####response
+ event
+ message
+ data


###签到
/api/v2/activity/check/
#####request
+ activity_id
+ team_id
#####response
+ event
+ message
+ data


###比赛过程中
/api/v2/activity/running/(?P<id>)/

###未完成队伍
/api/v2/activity/team/finish/
#####request
+ activity_id
#####response
+ event
+ message
+ data:{
  "finished":1,
  "unfinished":2
}

###排行榜
/api/v2/activity/rank/
#####request
+ activity_id

#####response
+ event
+ message
+ data:{
  "list":[Team,Team...];
}
