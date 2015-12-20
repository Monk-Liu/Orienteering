import tornado.web
from tornado import gen
import json
import database as DB
from database import User,UserInfo,Event,Points, UserEvent
from utils import encrytovalue
import base64
from collections import defaultdict
from random import randint


class BaseHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.session = DB.Session()
        self.redis = DB.Redis()

    def on_finish(self):
        self.session.close()


class JSONHandler(BaseHandler):

    def set_default_headers(self):
        self.set_header("Content-Type","application/json;charset=UTF-8")

    def prepare(self):
        self.res ={}
        self.json_args = defaultdict(lambda : '')
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
        self.write(json.dumps(self.res))
    
    def write_error(self,message):
        self.set_status(400,reason=message)
        self.res['message'] = message
        self.write(json.dumps(self.res))

class B64Handler(JSONHandler):

    def prepare(self):
        print (self.request.body)
        self.request.body = base64.b64decode(self.request.body)
        print(self.request.body)
        super(B64Handler,self).prepare()


class MixinHandler(object):

    def extract_user(self,info):
        self.res['nickname'] = info.nickname
        self.res['sex'] = info.sex
        self.res['age'] = info.age
        self.res['image'] = info.img_url

    def change_user(self,info):
        info.nickname = self.json_args['nickname']
        info.sex = self.json_args['sex']
        info.birthday = self.json_args['birthday']
        info.img_url  =self.json_args['image']

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
        e['title'] = event.title
        e['id'] = event.id
        e['during_time'] = event.during_time
        e['description'] = event.desc
        e['start_time'] = event.start_time
        e['loc_x'] = event.loc_x
        e['loc_y'] = event.loc_y
        e['loc_province'] = event.loc_province
        e['loc_city'] = event.loc_city
        e['loc_road'] = event.loc_road
        e['loc_distract'] = event.loc_distract
        e['person_limit'] = event.person_limit
        e['person_current'] = event.person_current
        e['logo'] = event.logo
        e['host'] = event.host
        e['type'] = event.type
        e['points'] = []
        try:
            for point in e.points:
                p = self.extract_point(point)
                e['points'].append(p)
        except Exception as exc:
            print(exc)
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
                self.res['key'] = user.id
                self.write_success()
            else:
                self.write_error('user or password not exist')
        else:
            self.write_error('arguments error')
            

class UserDetailHandler(JSONHandler, MixinHandler):


    def get(self,uid):
        user = self.session.query(User).get(uid)
        if user:
            self.extract_user(user.info[0])
            self.write_success()
        else:
            self.write_error('User not found')
    
    def post(self,uid):
        key = self.json_args['key']
        if uid==key:
            user = self.session.query(User).get(uid)
        else:
            user = {}
        if user:
            #use user's function to change info
            self.change_user(user.info[0])
            self.extract_user(user.info[0])
            self.session.add(user)
            self.session.commit()
            self.write_success()
        else:
            self.write_error('user not found')

class ActivitiesHandler(JSONHandler, MixinHandler):


    def get(self):
        province = self.get_argument('loc_province','')
        page = self.get_argument('page','')
        if province and page:
            try:
                page = int(page)
                page = page-1 if page else page
            except:
                page = 0
            self.res['list'] = []
            loc_events = self.session.query(Event).filter(Event.loc_province==province).\
                    offset(page*10).limit(10)
            if loc_events.count():
                for event in loc_events:
                    e = self.extract_event(event)
                    self.res['list'].append(e)
                # how to get hot?
            self.write_success()
        else:
            self.write_error("arguments error")

    def post(self):
        key = self.json_args['key']
        user = self.session.query(User).get(key)
        if user:
            event = Event(logo=user.info[0].img_url,
                        title       =self.json_args['title'],
                        during_time =self.json_args['during_time'],
                        desc        =self.json_args['description'],
                        loc_x       =self.json_args['loc_x'],
                        loc_y       =self.json_args['loc_y'],
                        loc_province=self.json_args['loc_province'],
                        loc_city    =self.json_args['loc_city'],
                        loc_distract=self.json_args['loc_distract'],
                        loc_road    =self.json_args['loc_road'],
                        person_limit=self.json_args['person_limit'],
                        start_time        =self.json_args['start_time'],
                        host        =user.info[0].id
                        )
            self.session.add(event)
            points = self.json_args['spotlist']
            if points:
                for p in points:
                    try:
                        point = Points(x    =p['x'],
                                    y       =p['y'],
                                    message =p['message'],
                                    radius  =p['radius'],
                                    order   =p['order'])
                        self.session.add(point)
                        event.points.append(point)
                    except:
                        self.res['message'] = 'some points error'
            else:
                event.points = []
            self.session.add(event)
            self.session.commit()
            self.write_success()
        else:
            self.write_error('permission denied')


class ActivityDetailHandler(JSONHandler, MixinHandler):
    
    def get(self):
        id = self.get_argument("activity_id","")
        key = self.get_argument("key","")
        if id and key:
            event = self.session.query(Event).get(id)
            if event :
                print(event.hoster.user_id,key)
                if event.hoster.user_id == key:
                    self.session.delete(event)
                    self.session.commit()
                    self.write_success()
                else:
                    self.write_error('permission denied')
            else:
                self.write_error('event not exists')
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
                    self.extract_evnet(event)
                    self.write_success()
                else:
                    self.write_error('user has already join the event')
            else:
                self.write_error('user or activity not exists')
        else:
            self.write_error("arguments error")

class CityHandler(JSONHandler):

    def __init__(self,*args,**kwargs):
        self.Province = ['湖北',"上海","浙江","北京","广东"]
        super(CityHandler,self).__init__(*args,**kwargs)

    def get(self):
        self.res['citylist'] = []
        #how should get the data?
        for i in range(5):
            p = {}
            p["province_name"] = self.Province[i]
            p["cities"] = []

            for j in range(randint(1,4)):
                p['cities'].append({"code":"000"+str(j*i),"city":"city "+str(j)})
            self.res['citylist'].append(p)
        self.write_success()

class SplashHandler(JSONHandler):

    def get(self):
        self.res['url'] = '/static/common.jpg'
        self.write_success()

class UserHostHandler(JSONHandler, MixinHandler):

    def get(self):
        key = self.get_argument('key','')
        if key:
            user = self.session.query(User).get(key)
            if user:
                self.res['list'] = []
                for event in user.info[0].host_event:
                    e = self.extract_event(event)
                    self.res['list'].append(e)
                self.write_success()
            else:
                self.write_error('user not exists')
        else:
            self.write_eror('No match pattern found')

class UserAttendHandler(JSONHandler, MixinHandler):

    def get(self):
        key = self.get_argument('key','')
        if key:
            user = self.session.query(User).get(key)
            if user:
                self.res['list'] = []
                for event in user.info[0].join_event:
                    e = self.extract_event(event.the_event)
                    self.res['list'].append(e)
                self.write_success()
            else:
                self.write_error("user not exist")
        else:
            self.write_error('arguments error')

    def post(self):
        key = self.json_args['key']
        activity_id = self.json_args['activity_id']
        if key and activity_id:
            user = self.session.query(User).get(key)
            event = self.session.query(Event).get(activity_id)
            if user and event:
                event.userinfo_id.append(user)
                self.merge(event)
                self.write_success()
            else:
                self.write_error('user or event not exists')
        else:
            self.write_error('arguments error')


class ActivityAttendHandler(JSONHandler, MixinHandler):

    def get(self):
        id = self.get_argument('activity_id','')
        if id :
            event = self.session.query(Event).get(id)
            if event:
                self.res['person_list'] = []
                for person in event.userinfo_id:
                    p = {}
                    p['name'] = person.the_user.nickname
                    p['key'] = person.the_user.user_id
                    self.res['person_list'].append(p)
                self.write_success()
            else:
                self.write_error("activity not exist")
        else:
            self.write_error("arguments error")

    def post(self):
        id = self.json_args.get('activity_id')
        key = self.json_args['key']
        finish_time = self.json_args['finish_time']
        reached_spotlist = self.json_args['reached_spotlist']
        if id and key and reached_spotlist and reached_spotlist:
            user = self.session.query(User).get(key)
            event = self.session.query(Event).get(id)
            userevent = user.info[0].join_event
            if event and user and event.id in (event.event_id for event in userevent):
                userevent.finish_time = finish_time
                finish_points = 0
                for point in reached_spotlist:
                    finish_points += 2**point['order']
                userevent.finish_points =  finish_points
                self.session.merge(user)
                self.session.merge(event)
                self.session.commit()
                self.write_success()
            else:
                self.write_error('user have not attend the activity')
        else:
            self.write_error('arguments error')
