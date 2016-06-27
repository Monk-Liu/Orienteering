import tornado.web
from tornado import gen
import json
import database as DB
from database import RedisOne, RedisTwo
from database import User,UserInfo,Event,Points,Team, OAuthor, PointToTeam, Members
from utils import encrytovalue
import base64
from collections import defaultdict
from random import randint
from config import CITIES
import time

class BaseHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.session = DB.Session()
        #self.redis = DB.Redis()

    def on_finish(self):
        self.session.close()


class JSONHandler(BaseHandler):

    def set_default_headers(self):
        self.set_header("Content-Type","application/json;charset=UTF-8")

    def prepare(self):
        self.response ={}
        self.res = None
        self.json_args = defaultdict(lambda : None)
        #the defaultdict is used for avoid Key Error situation
        if self.request.method not in ("GET","HEAD"):
            try:
                body = self.request.body.decode('utf8')
                if body:
                    json_args = json.loads(body)
                else:
                    json_args = None
                for key,value in json_args.items():
                    self.json_args[key] = value
            except Exception as e:
                print("json arguments error",e)

    def write_success(self,code=0):
        self.response['event'] = code
        self.response['message'] = ''
        self.response['data'] = self.res
        self.write(json.dumps(self.response))
    
    def write_error(self,message,code=400):
        #self.set_status(code,reason=message)
        self.response['event'] = 1 if code==400 else 2 if code==403 else 3
        self.response['message'] = message
        self.response['data'] = self.res
        #if 'data' in self.response.keys():
        #    self.response.pop("data")
        self.write(json.dumps(self.response))

class B64Handler(JSONHandler):

    def prepare(self):
        self.request.body = base64.urlsafe_b64decode(self.request.body)
        super(B64Handler,self).prepare()


#TODO 改字段
class MixinHandler(object):

    def extract_user(self,info):
        self.res = {}
        self.res['nickname'] = info.nickname
        self.res['sex'] = info.sex
        self.res['birthday'] = info.birthday
        self.res['avatar'] = info.img_url
        self.res['weight'] = info.weight
        self.res['height'] = info.height
        self.res['address'] = info.area

    def change_user(self,info):
        info.nickname = self.json_args['nickname']
        info.sex = self.json_args['sex']
        info.birthday = self.json_args['birthday']
        info.img_url  =self.json_args['avatar']
        info.weight = self.json_args['weight']
        info.height = self.json_args['height']
        info.area = self.json_args['address']

    def extract_point(self, point):
        p = {}
        p['id'] = point.id
        p['x'] = point.x
        p['y'] = point.y
        p['message'] = point.message
        p['type'] = point.type
        p['radius'] = point.radius
        p['pwd'] = point.pwd
        return p

    def extract_event(self,event):
        e = {}
        e["name"] = event.title
        e['id'] = event.id
        e['apply_start'] = event.apply_start
        e['description'] = event.description
        e['apply_end'] = event.apply_end
        e['loc_x'] = event.loc_x
        e['loc_y'] = event.loc_y
        e['loc_province'] = event.loc_province
        e['loc_city'] = event.loc_city
        e['loc_road'] = event.loc_road
        e['loc_district'] = event.loc_distract
        e['person_limit'] = event.person_limit
        e['person_current'] = event.person_current
        e['logo'] = event.logo
        e['type'] = event.type
        e['spotlist'] = []
        e['game_start'] = event.game_start
        e['game_end'] = event.game_end
        e['person_per_team'] = event.person_per_team
        e['prize'] = event.prize

        for point in event.points:
            p = self.extract_point(point)
            e['spotlist'].append(p)
        host = self.session.query(UserInfo).get(event.host)
        if host:
            e['host'] = host.nickname
        else:
            e['host'] = " "
        return e



class UserHandler(B64Handler):
    
    def get(self):
        pass

    def post(self):
        phone = self.json_args['phone']
        password = self.json_args['password']
        user_id = self.json_args['user_id']
        if phone and password:
            #query.get 后判断和 query.filter 的区别
            if not user_id:
                user_query = self.session.query(User).filter(User.phone==phone,
                                                  User.password==encrytovalue(password))
                if user_query.count():
                    user = user_query.first()
                    self.res = user.id
                    self.write_success()
                else:
                    self.write_error('user or password not exist',401)
            else:
                user = self.session.query(OAuthor).get(user_id)
                if user:
                    self.res = user.id
                    self.write_success()
                else:
                    self.write_error("user not found", 404)
        else:
            self.write_error('arguments error')
            

class UserDetailHandler(JSONHandler, MixinHandler):


    def get(self,uid):
        if uid:
            user = self.session.query(User).get(uid)
        #else:
        #    key = self.json_args["key"]
        #    user = self.session.query(User).get(uid)
        if user:
            self.extract_user(user.info[0])
            self.write_success()
        else:
            self.write_error('User not found',404)
    
    def post(self,uid):
        key = self.json_args['key']
        if uid==key:
            user = self.session.query(User).get(uid)
        else:
            user = {}
        if user:
            #use user's function to change info
            self.change_user(user.info[0])
            #self.extract_user(user.info[0])
            self.session.merge(user)
            self.session.merge(user.info[0])
            self.session.commit()
            self.write_success()
        else:
            self.write_error('user not found',404)

class ActivitiesHandler(JSONHandler, MixinHandler):


    #TODO:: 个人赛和团体赛
    #TODO:: 比赛排序
    def get(self):
        province = self.get_argument('loc_province','')
        page = self.get_argument('page','')
        if province and page:
            try:
                page = int(page)
                page = page-1 if page else page
            except:
                page = 0
            self.res = []
            loc_events = self.session.query(Event).filter(Event.loc_province==province).\
                order_by(Event.game_start.desc()).offset(page*10).limit(10)
            if loc_events.count():
                for event in loc_events:
                    e = self.extract_event(event)
                    self.res.append(e)
                # how to get hot?
            self.write_success()
        else:
            self.write_error("arguments error")

    def post(self):
        #key = self.json_args['key']
        key = self.get_argument("key",'')
        if key:
            user = self.session.query(User).get(key)
        else:
            user = None
        if user and not self.json_args['id']:
            event = Event(
                        title       =self.json_args['name'],
                        apply_start =self.json_args['apply_start'],
                        apply_end   =self.json_args['apply_end'],
                        game_start  =self.json_args['game_start'],
                        game_end    =self.json_args['game_end'],
                        desc        =self.json_args['description'],
                        loc_x       =self.json_args['loc_x'],
                        loc_y       =self.json_args['loc_y'],
                        loc_province=self.json_args['loc_province'],
                        loc_city    =self.json_args['loc_city'],
                        loc_distract=self.json_args['loc_district'],
                        loc_road    =self.json_args['loc_road'],
                        person_limit=self.json_args['person_limit'],
                        person_per_team = self.json_args['person_per_team'],
                        prize       =self.json_args['prize'],
                        host        =user.info[0].id,
                        type        =self.json_args['type']
                        )
            self.session.add(event)
            points = self.json_args['spotlist']

            if points:
                for p in points:
                    point = Points(x    =p['x'],
                                    y       =p['y'],
                                    message =p['message'],
                                    radius  =p['radius'],
                                    type   =p['type'])
                    self.session.add(point)
                    event.points.append(point)
                    #except:
                    #    self.write_error('point error')
            else:
                event.points = []
            self.session.add(event)
            self.session.commit()
            self.res = event.id
            self.write_success()
        elif user and self.json_args['id']:
            event = self.session.query(Event).get(self.json_args['id'])
            if event:
                event.logo = self.json_args['logo']
                #event.title       =self.json_args['name']
                #event.during_time =self.json_args['end_time']
                #event.desc        =self.json_args['description']
                #event.loc_x       =self.json_args['loc_x']
                #event.loc_y       =self.json_args['loc_y']
                #event.loc_province=self.json_args['loc_province']
                #event.loc_city    =self.json_args['loc_city']
                #event.loc_distract=self.json_args['loc_distract']
                #event.loc_road    =self.json_args['loc_road']
                #event.person_limit=self.json_args['person_limit']
                #event.start_time        =self.json_args['start_time']
                #event.host        =user.info[0].id
                self.session.merge(event)
                self.session.commit()
                self.res = event.id
                self.write_success()
            else:
                self.write_error("event not found", code=404)
        else:
            self.write_error('permission denied', 403)


class ActivityDetailHandler(JSONHandler, MixinHandler):
    
    def get(self):
        id = self.get_argument("activity_id","")
        key = self.get_argument("key","")
        if id and key:
            event = self.session.query(Event).get(id)
            if event :
                if event.hoster.user_id == key:
                    self.session.delete(event)
                    self.session.commit()
                    self.write_success()
                else:
                    self.write_error('permission denied', 403)
            else:
                self.write_error('event not exists',404)
        else:
            self.write_error("arguments error")
            

#TODO 报名
    def post(self):
        key = self.json_args["key"]
        id = self.json_args["activity_id"]
        if key and id:
            user = self.session.query(User).get(key)
            event = self.session.query(Event).get(id)
            if user and event:
                info = user.info[0]
                if event.id not in (event.event_id for event in info.join_event):
                    team = Team()
                    team.name = info.nickname
                    team.event = event
                    info.join_event.append(team)
                    event.person_current += 1
                    self.session.merge(user)
                    self.session.merge(event)
                    self.session.commit()
                    #self.extract_event(event)
                    self.write_success()
                else:
                    self.write_error('user has already join the event', 401,)
            else:
                self.write_error('user or activity not exists', 404)
        else:
            self.write_error("arguments error")


class UserHostHandler(JSONHandler, MixinHandler):

    def get(self):
        key = self.get_argument('key','')
        if key:
            user = self.session.query(User).get(key)
            if user:
                self.res = []
                for event in user.info[0].host_event:
                    e = self.extract_event(event)
                    self.res.append(e)
                self.write_success()
            else:
                self.write_error('user not exists',404)
        else:
            self.write_error('No match pattern found')



class UserAttendHandler(JSONHandler, MixinHandler):

    def get(self):
        key = self.get_argument('key','')
        if key:
            user = self.session.query(User).get(key)
            if user:
                self.res = []
                for event in user.info[0].join_event:
                    e = self.extract_event(event.event)
                    self.res.append(e)
                self.write_success()
            else:
                self.write_error("user not exist", 404)
        else:
            self.write_error('arguments error')

   #TODO 取消报名
    def post(self):
        key = self.json_args['key']
        activity_id = self.json_args['activity_id']
        if key and activity_id:
            user = self.session.query(User).get(key)
            event = self.session.query(Event).get(activity_id)
            if user and event:
                teams = user.info[0].join_event
                for team in teams:
                    if team.event_id == event.id:
                        user.info[0].join_event.remove(team)
                        event.userinfo_id.remove(team)
                        self.session.delete(team)
                        break
                self.session.merge(event)
                self.session.merge(user)
                self.session.commit()
                self.write_success()
            else:
                self.write_error('user or event not exists', 404)
        else:
            self.write_error('arguments error')


class ActivityAttendHandler(JSONHandler, MixinHandler):

    #TODO:: 个人赛和团体赛报名

    #参加活动用户
    def get(self):
        id = self.get_argument('activity_id','')
        if id :
            event = self.session.query(Event).get(id)
            if event:
                self.res = []
                for team in event.teams:
                    p = {}
                    captain = team.captain
                    p['name'] = captain.nickname
                    p['key'] = captain.user_id
                    self.res.append(p)
                self.write_success()
            else:
                self.write_error("activity not exist", 404)
        else:
            self.write_error("arguments error")


    #个人赛完成一个点
    def post(self):
        id = self.json_args.get('activity_id')
        key = self.json_args['key']
        finish_time = self.json_args['during_time'] # finish -> during_time
        reached_spotlist = self.json_args['reached_spotlist']
        if id and key and reached_spotlist and reached_spotlist:
            user = self.session.query(User).get(key)
            event = self.session.query(Event).get(id)
            team = user.info[0].join_event if user else []
            if event and user:
                for the_event in team:
                    if the_event.event_id == event.id:
                        the_event.finish_time = finish_time
                        finish_points = 0
                        for point in reached_spotlist:
                            finish_points += 2**point
                            the_event.finish_points =  finish_points
                self.session.merge(user)
                self.session.merge(event)
                self.session.commit()
                self.write_success()
            else:
                self.write_error('user have not attend the activity', 401)
        else:
            self.write_error('arguments error')


# 记录到一个点
#完成的比赛
class ActivityFinishHandler(JSONHandler):

    def get_point(self, n):
        spotlist = []
        i = 0
        while n:
            if n&1:
                spotlist.append(i)
            i += 1
            n = n>>1
        return spotlist
    
    #显示用户完成的比赛
    def get(self):
        key = self.get_argument("key", '')
        if key:
            user = self.session.query(User).get(key)
            if user:
                self.res = []
                info = user.info[0]
                for team in info.join_event:
                    if team.finish_points != 0:
                        event = {}
                        event['id'] = team.event_id
                        event['during_time'] = team.finish_time
                        event['reached_spotlist'] = self.get_point(team.finish_points)
                        self.res.append(event)
                self.write_success()
            else:
                self.write_error("user not exists", 404)
        else:
            self.write_error("arguments error")


    def post(self):
        activity_id = self.json_args['activity_id']
        if activity_id:
            event = self.session.query(Event).get(activity_id)
            if event:
                for team in event.userinfo_id:
                    self.res = []
        else:
            self.write_error('arguments')

class OAuthorHandler(JSONHandler):

    def post(self):
        openid = self.json_args['openid']
        if openid:
            user = self.session.query(OAuthor).get(openid)
            if user:
                u = self.session.query(User).get(user.id)
                if u and u.phone:
                    self.res = user.id
                    self.write_success(code=5)
                else:
                    self.res = user.id
                    self.write_success()
            else:
                author = OAuthor(openid)
                user = User(id=author.id)
                userinfo = UserInfo()
                user.info.append(userinfo)
                self.session.add(user)
                self.session.add(author)
                self.session.commit()
                self.res = author.id
                self.write_success()
        else:
            self.write_error('arguments error')

## 团队赛报名 
class TeamHandler(JSONHandler):

## 取消报名
    def get(self):
        team_id = self.get_argument('team_id','')
        key = self.get_argument("key",'')
        if  key and team_id:
            team = self.session.query(Team).get(team_id)
            if team.captain.user_id == key:
                for member in team.members:
                    self.session.delete(member)
                team.event.person_current = team.event.person_current -1
                self.session.delete(team)
                self.session.merge(team.event)
                self.session.commit()
                self.write_success()
            else:
                self.write_error("permission deny",403)
        else:
            self.write_error("arguments error", 400)

#创建队伍
    def post(self):
        id = self.json_args['activity_id']
        key = self.json_args['key']
        name = self.json_args['name']
        urgent_contact = self.json_args['urgent_contact']
        slogan = self.json_args['slogan']
        urgent_phone = self.json_args['urgent_phone']
        members = self.json_args['members']
        if id and key :
            event = self.session.query(Event).get(id)
            user = self.session.query(User).get(key)
            if event and user and event.person_current<event.person_limit:
                team = Team(
                            slogan=slogan,
                            urgent_contact=urgent_contact,
                            urgent_phone=urgent_phone,
                           )
                team.name = name
                user.info[0].join_event.append(team)
                event.teams.append(team)
                for member in members:
                    m = Members(name=member['name'],
                                idcard=member['idcard'],
                                gender=member['sex'],
                                phone=member['phone'])
                    team.members.append(m)
                event.person_current += 1
                self.session.add(team)
                self.session.merge(user.info[0])
                self.session.merge(event)
                self.session.commit()
                self.write_success()
            else:
                self.write_error("No such event or team number limited")
        else:
            self.write_error("argument error")

class MemberHandler(JSONHandler):

    def get(self):
        activity_id = self.get_argument("activity_id",'')
        key = self.get_argument("key",'')
        if key and activity_id:
            user = self.session.query(User).get(key)
            if user:
                phone = user.phone
            else:
                phone = ''
            members = self.session.query(Members).filter(Members.phone==phone)
            print(members.count())
            if members.count():
                for member in members:
                    if member.team.event_id == activity_id:
                        self.res = member.team_id
                        break
                    else:
                        self.res = -1
            else:
                self.res =  -1
            self.write_success()
        else:
            self.write_error("arguemnt_error")

class TeamDetailHandler(JSONHandler):

    def get(self):
        team_id = self.get_argument('team_id','')
        if team_id:
            team = self.session.query(Team).get(team_id)
            if team:
                #try:
                    self.res = {}
                    self.res['id'] = team.id
                    self.res['activity_id'] = team.event_id
                    self.res['name'] = team.name
                    self.res['urgent_contact'] = team.urgent_contact
                    self.res['urgent_phone'] = team.urgent_phone
                    self.res['key'] = team.captain.user_id
                    self.res['check'] = True if team.check else False
                    self.res['slogan'] = team.slogan
                    self.res['members'] = []
                    captain_phone = team.captain.user.phone
                    for member in team.members:
                        m = {}
                        m['name'] = member.name
                        m['idcard'] = member.idcard
                        m['gender'] = member.gender
                        m['phone'] = member.phone
                        if m['phone'] == captain_phone:
                            self.res['members'].insert(0,m)
                        else:
                            self.res['members'].append(m)
                    self.write_success()
                #except:
                #    self.write_error("phone repeat")
            else:
                self.write_error("Not Found that team")
        else:
            self.write_error("arguments error")


##### 签到以及显示签到
class CheckHandler(JSONHandler):

    def get(self):
        team_id = self.json_args['team_id']
        if team_id:
            team = self.session.query(Team).get(team_id)
            if team and team.event_id == id:
                self.res = True
            else:
                self.res = False
            self.write_success()
        else:
            self.write("something wrong")

    def post(self):
        id = self.json_args['activity_id']
        team_id = self.json_args['team_id']
        team_id = int(team_id)
        team = self.session.query(Team).get(team_id)
        if team and team.event_id==id:
            team.check = 1
            self.session.merge(team)
            self.session.commit()
            self.write_success()
        else:
            self.write_error("something wrong")

class RunningHandler(JSONHandler):

    def get(self):
        team_id = self.get_argument('team_id','')
        if team_id:
            team = self.session.query(Team).get(team_id)
            if team:
                self.res = 1 if team.is_run else 0
                self.write_success()
            else:
                self.write_error("team not found",404)
        else:
            self.write_error("argument error", 400)


    def post(self):
        user_id = self.json_args["key"]
        team_id = self.json_args["team_id"]
        if user_id and team_id:
            team = self.session.query(Team).get(team_id)
            if team and team.captain.user_id == user_id:
                team.is_run = 1
                self.write_success()
            else:
                self.write_error("permition deny", 403)
        else:
            self.write_error("arguemnt error")

class PointArriveHandler(JSONHandler):

    def get(self):
        pass

    def post(self):
        point_id = self.json_args['point_id']
        team_id = self.json_args['team_id']
        finish_time = self.json_args['finish_time']
        if point_id:
            point = self.session.query(Points).get(point_id)
            if point:
                for r_team in point.teamlist:
                    if r_team.team_id == team_id:
                        r_team.time = time.strftime("%H:%M:%S") # bug may exist here?
                        self.session.merge(r_team)
                        break
                self.session.merge(point)
                self.session.commit()
                self.write_success()
            else:
                self.write_error("something wrong")
        else:
            self.write_error("argument error")

class FinishTeamHandler(JSONHandler):

    def get(self):
        activity_id = self.get_argument("activity_id")
        if activity_id:
            event = self.session.query(Event).get(activity_id)
            if event:
                team_finished = 0
                team_unfinished = 0
                for team in event.teams:
                    if team.finish_points != 0:
                        team_finished += 1
                    else:
                        team_unfinished += 1
                self.res = {}
                self.res['finished'] = team_finished
                self.res['unfinished'] = team_unfinished
                self.write_success()
            else:
                self.write_error("No such event", 404)
        else:
            self.write_error("arguments error")

class RankListHandler(JSONHandler):

    def get(self):
        activity_id = self.get_argument("activity_id")
        if activity_id:
            event = self.session.query(Event).get(activity_id)
            if event:
                self.res = []
                for team in event.teams:
                    t = {}
                    t['name'] = team.name
                    t['slogan'] = team.slogan
                    t['score'] = team.score
                    self.res.append(t)
                self.write_success()

            else:
                self.write_error("No such event")
        else:
            self.write_error("arguemnts error")

class RealTimeHandler(JSONHandler):

    def initialize(self):
        self.redis = RedisOne()

    def on_finish(self):
        pass
    
    def get(self, id):
        pass # 把数据存到redis里面去

    def post(self, activity_id):
        ismaster = self.json_args['is_master']
        _type = self.json_args['type']
        x = self.json_args['x']
        y = self.json_args['y']
        message = self.json_args['message']
        _index = self.json_args['index']
        _time = self.json_args['time']
        team_id = self.json_args['team_id']
        #with open("log.txt","w+") as f:
        #    f.write(self.request.body.decode())
        #    f.write('sadfadf')
        if ismaster:
            if x and y and team_id and _time:
                _index = str(_index)
                _type = str(_type)
                team_id = str(team_id)
                _time  = str(_time)
                #type == "complete"  import all data for the team in redis
                if _type==2: # finish
                    pass
                if message:
                    message = message.replace("#",",")
                else:
                    message = ''
                data = "#".join([_type,_time,team_id,x,y,message,_index])
                #存到redis
                keyname = activity_id + team_id
                key = self.redis.keys(keyname)
                if not key:
                    self.redis.rpush(keyname,data)
                    self.redis.expire(keyname,int(time.time()+86400))
                else:
                    self.redis.rpush(keyname,data)
            else:
                self.response["message"] = "x y index is invalid"
        self.res = [] # 获得数据
        data = self.redis.keys(activity_id+"*")
        for ele in data:
            e = {}
            re_str = self.redis.lrange(ele,-1,-1)[0]
            _list = re_str.decode("utf8").split("#")
            e['team_id'] = _list[2]
            e['x'] = _list[3]
            e['y'] = _list[4]
            self.res.append(e)
        self.write_success()
        # 还是和 post 写一起吧 这样就少了一倍的并发了是吧？

class CityHandler(JSONHandler):

    def get(self):
        self.res = CITIES
        self.write_success()

class DisclaimerHandler(JSONHandler):

    def get(self):
        self.redis = RedisTwo()

        disclaimer = self.redis.get("disclaimer")
        self.res = disclaimer.decode()
        self.write_success()

class SplashHandler(JSONHandler):

    def get(self):
        self.res = 'https://c1.staticflickr.com/3/2474/5744485713_9f1573f0cd_b.jpg'
        self.write_success()

class NotFoundHandler(JSONHandler):

    def get(self):
        self.write_error("Not Found",404)

    def post(self):
        self.write_error("NotFound",404)

