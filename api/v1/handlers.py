import tornado.web
from tornado import gen
import json
import database as DB
from database import User,UserInfo,Event,Points
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
                print("json arguments error")

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
        for point in e.points:
            p = self.extract_point(point)
            e['points'].append(p)
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
            self.extract_user(user)
            self.session.commit()
            self.write_success()
        else:
            self.write_error('user not found')

class ActivitiesHandler(JSONHandler, MixinHandler):


    def get(self):
        province = self.get_argument('loc_province','')
        page = self.get_argument('page','')
        if province and page:
            self.res['list'] = []
            try:
                page = int(page)
                page = page-1 if page else page
            except:
                page = 0
            loc_events = self.session.query(Event).filter('loc_province'==province).\
                    offset(page*10).limit(10)
            if loc_events.count():
                for event in loc_events:
                    e = self.extract_event(event)
                    self.res['list'].append(e)
                self.write_success()
                # how to get hot?
            else:
                self.write_error('not activity')

    def post(self):
        key = self.json_args['key']
        user = self.session.get(key)
        if user:
            during_time = self.json_args['during_time']
            event = Event(logo=user.info[0].img_url,
                        title       ='',
                        during_time  =during_time,
                        desc        =self.json_args['description'],
                        loc_x       =self.json_args['loc_x'],
                        loc_y       =self.json_arg['loc_y'],
                        loc_province=self.json_args['loc_province'],
                        loc_city    =self.json_args['loc_city'],
                        loc_distract=self.json_args['loc_distract'],
                        loc_road    =self.json_args['loc_road'],
                        person_limit=self.json_args['person_limit'],
                        start_time        =self.json_args['start_time'],
                        host        =user.info[0].id
                        )
            for p in self.json_args['points']:
                try:
                    point = Points(x    =p['x'],
                                y       =p['y'],
                                message =p['message'],
                                radius  =p['radius'],
                                order   =p['order'])
                    event.points.append(point)
                except:
                    self.write_error('some points error')
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
                if event.host.user.id == key:
                    event.delete()
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
                if event not in user.info.join_event:
                    user.info.join_event.append(event)
                    self.session.merge(user)
                    self.session.merge(event)
                    self.session.commit()
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

class UserHostHandler(JSONHandler):

    def get(self):
        key = self.get_argument('key','')
        if key:
            user = self.session.query(User).get(key)
            if user:
                self.res['list'] = []
                for event in user.info.host_event:
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
                for event in user.info.join_event:
                    e = self.extract_event(event)
                    self.res['list'].append(e)
                self.write_success()
            else:
                self.write_error("user not exist")
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
                    p['name'] = person.nickname
                    p['key'] = person.user_id.id
                    self.res['person_list'].append(p)
                self.write_success()
            else:
                self.write_error("activity not exist")
        else:
            self.write_error("arguments error")
