import tornado.web
from tornado import gen
import json
import database as DB
from database import User,UserInfo,Event,Points, UserEvent, OAuthor
from utils import encrytovalue
import base64
from collections import defaultdict
from random import randint
from config import CITIES

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

    def write_success(self):
        self.response['event'] = 0
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
        p['x'] = point.x
        p['y'] = point.y
        p['message'] = point.message
        p['type'] = point.type
        p['radius'] = point.radius
        p['order'] = point.order
        return p

    def extract_event(self,event):
        e = {}
        e["name"] = event.title
        e['id'] = event.id
        e['end_time'] = event.during_time
        e['description'] = event.desc
        e['start_time'] = event.start_time
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
        for point in event.points:
            print(point.order)
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
        if phone and password:
            #query.get 后判断和 query.filter 的区别
            user_query = self.session.query(User).filter(User.phone==phone,
                                                  User.password==encrytovalue(password))
            if user_query.count():
                user = user_query.first()
                self.res = user.id
                self.write_success()
            else:
                self.write_error('user or password not exist',401)
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
                    offset(page*10).limit(10)
            if loc_events.count():
                for event in loc_events:
                    e = self.extract_event(event)
                    self.res.append(e)
                # how to get hot?
            self.write_success()
        else:
            self.write_error("arguments error")

    def post(self):
        key = self.get_argument('key','')
        if key:
            user = self.session.query(User).get(key)
        else:
            user = None
        if user and not self.json_args['id']:
            event = Event(
                        title       =self.json_args['name'],
                        during_time =self.json_args['end_time'],
                        desc        =self.json_args['description'],
                        loc_x       =self.json_args['loc_x'],
                        loc_y       =self.json_args['loc_y'],
                        loc_province=self.json_args['loc_province'],
                        loc_city    =self.json_args['loc_city'],
                        loc_distract=self.json_args['loc_district'],
                        loc_road    =self.json_args['loc_road'],
                        person_limit=self.json_args['person_limit'],
                        start_time        =self.json_args['start_time'],
                        host        =user.info[0].id
                        )
            self.session.add(event)
            points = self.json_args['spotlist']

            if points:
                order = 0
                for p in points:
                    point = Points(x    =p['x'],
                                    y       =p['y'],
                                    message =p['message'],
                                    radius  =p['radius'],
                                    order = order,
                                    type   =p['type'])
                    self.session.add(point)
                    event.points.append(point)
                    order += 1
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
                event.title       =self.json_args['name']
                event.during_time =self.json_args['end_time']
                event.desc        =self.json_args['description']
                event.loc_x       =self.json_args['loc_x']
                event.loc_y       =self.json_args['loc_y']
                event.loc_province=self.json_args['loc_province']
                event.loc_city    =self.json_args['loc_city']
                event.loc_distract=self.json_args['loc_distract']
                event.loc_road    =self.json_args['loc_road']
                event.person_limit=self.json_args['person_limit']
                event.start_time        =self.json_args['start_time']
                event.host        =user.info[0].id
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
            

    def post(self):
        key = self.json_args["key"]
        id = self.json_args["activity_id"]
        if key and id:
            user = self.session.query(User).get(key)
            event = self.session.query(Event).get(id)
            if user and event:
                info = user.info[0]
                if event.id not in (event.event_id for event in info.join_event):
                    userevent = UserEvent()
                    userevent.event = event
                    info.join_event.append(userevent)
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

class CityHandler(JSONHandler):

    def get(self):
        self.res = CITIES
        self.write_success()

class SplashHandler(JSONHandler):

    def get(self):
        self.res = 'https://c1.staticflickr.com/3/2474/5744485713_9f1573f0cd_b.jpg'
        self.write_success()

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
                    e = self.extract_event(event.the_event)
                    self.res.append(e)
                self.write_success()
            else:
                self.write_error("user not exist", 404)
        else:
            self.write_error('arguments error')

    def post(self):
        key = self.json_args['key']
        activity_id = self.json_args['activity_id']
        if key and activity_id:
            user = self.session.query(User).get(key)
            event = self.session.query(Event).get(activity_id)
            if user and event:
                userevents = user.info[0].join_event
                for userevent in userevents:
                    if userevent.the_event.id == event.id:
                        user.info[0].join_event.remove(userevent)
                        event.userinfo_id.remove(userevent)
                        self.session.delete(userevent)
                        break
                self.merge(event)
                self.metge(user)
                self.session.commit()
                self.write_success()
            else:
                self.write_error('user or event not exists', 404)
        else:
            self.write_error('arguments error')


class ActivityAttendHandler(JSONHandler, MixinHandler):

    #TODO:: 个人赛和团体赛报名

    def get(self):
        id = self.get_argument('activity_id','')
        if id :
            event = self.session.query(Event).get(id)
            if event:
                self.res = []
                for userevent in event.userinfo_id:
                    p = {}
                    p['name'] = userevent.the_user.nickname
                    p['key'] = userevent.the_user.user_id
                    self.res.append(p)
                self.write_success()
            else:
                self.write_error("activity not exist", 404)
        else:
            self.write_error("arguments error")


    def post(self):
        id = self.json_args.get('activity_id')
        key = self.json_args['key']
        finish_time = self.json_args['during_time'] # finish -> during_time
        reached_spotlist = self.json_args['reached_spotlist']
        if id and key and reached_spotlist and reached_spotlist:
            user = self.session.query(User).get(key)
            event = self.session.query(Event).get(id)
            userevent = user.info[0].join_event if user else []
            if event and user:
                for the_event in userevent:
                    if the_event.event_id == event.id:
                        the_event   .finish_time = finish_time
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

    def get(self):
        key = self.get_argument("key", '')
        if key:
            user = self.session.query(User).get(key)
            if user:
                self.res = []
                info = user.info[0]
                for userevent in info.join_event:
                    if userevent.finish_points != 0:
                        event = {}
                        event['id'] = userevent.event.id
                        event['during_time'] = userevent.finish_time
                        event['reached_spotlist'] = self.get_point(userevent.finish_points)
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
                for userevent in event.userinfo_id:
                    self.res = []
        else:
            self.write_error('arguments')

class OAuthorHandler(JSONHandler):

    def post(self):
        openid = self.json_args['openid']
        if openid:
            user = self.session.query(OAuthor).get(openid)
            if user:
                self.res = user.id
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


class NotFoundHandler(JSONHandler):

    def get(self):
        self.write_error("Not Found",404)

    def post(self):
        self.write_error("NotFound",404)
