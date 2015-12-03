import tornado.web
from tornado import gen
from tornado import httpclient
import json
import database as DB
from database import User,UserInfo,Event,Points
from utils import encrytovalue

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
        self.res['data'] = {}
        if self.request.method not in ("GET","HEAD"):
            try:
                body = self.request.body.decode('utf8')
                if body:
                    self.json_args = json.loads(body)
                else:
                    self.json_args = None
                print(self.json_args)
            except Exception as e:
                print("json arguments error")

    def write_success(self):
        self.res['status'] = 1
        self.write(json.dumps(self.res))
    
    def write_error(self,mesg):
        self.res['status'] = 2
        self.res['mesg'] = mesg
        self.write(json.dumps(self.res))


class UserHandler(JSONHandler):
    
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
                self.res['data']['key'] = user.id
                self.write_success()
            else:
                self.write_error('user or password not exist')
        else:
            self.write_error('arguments error')
            

class UserDetailHandler(JSONHandler):

    def extract_user(self,info):
        self.res['data']['nickname'] = info.nickname
        self.res['data']['sex'] = info.sex
        self.res['data']['age'] = info.age
        self.res['data']['img_url'] = info.img_url
        
    def change_user(self,info):
        info.nickname = self.json_args['nickname']
        info.sex = self.json_args['sex']
        info.age = self.json_args['age']
        info.img_url  =self.json_args['img_url']

    def get(self,uid):
        user = self.session.query(User).get(uid)
        print(user)
        if user:
            self.extract_user(user.info[0])
            self.res['status'] = 1
            self.write_success()
        else:
            self.write_error('User not found')
    
    def put(self,uid):
        key = self.json_args['key']
        print(uid,key)
        if uid==key:
            user = self.session.query(User).get(uid)
        else:
            user = {}
        if user:
            #use user's function to change info
            self.change_user(user.info[0])
            self.session.merge(user)
            self.extract_user(user)
            self.session.commit()
            self.res['status'] = 1
            self.write_success()
        else:
            self.write_error('user not found')

class ActivityHandler(JSONHandler):

    def get(self):
        province = self.get_argument('loc_province','')
        if province:
            events = self.session.query(Event).filter('loc_province'==province).limit(10)
            if events.count():
                for event in events:
                    e = {}
                    e['title'] = event.title
                    e['desc'] = event.desc
                    e['date'] = event.date
                    e['loc_x'] = event.loc_x
                    e['loc_y'] = event.loc_y
                    e['loc_province'] = event.loc_province
                    e['loc_city'] = event.loc_city
                    e['loc_road'] = event.loc_road
                    e['loc_distract'] = event.loc_distract
                    e['people_limit'] = event.people_limit
                    e['people_current'] = event.people_current
                    e['logo'] = event.logo
                    e['host'] = event.host
                    e['points'] = []
                    for point in e.points:
                        p = {}
                        p['x'] = point.x
                        p['y'] = point.y
                        p['message'] = point.message
                        p['type'] = point.type
                        p['radius'] = point.radius
                        e['points'].append(p)
                    self.res['data'].append(e)
                self.write_success()
            else:
                self.write_error('not activity')

    def post(self):
        key = self.json_args['key']
        user = self.session.get(key)
        if user:
            event = Event(logo=user.info[0].img_url,
                        title='',
                        desc=self.json_args['description'],
                        loc_x=self.json_args['loc_x'],
                        loc_y=self.json_arg['loc_y'],
                        loc_province=self.json_args['loc_province'],
                        loc_city=self.json_args['loc_city'],
                        loc_distract=self.json_args['loc_distract'],
                        loc_road=self.json_args['loc_road'],
                        people_limit=self.json_args['people_limit'],
                        date=self.json_args['time'],
                        host=user.info[0].id
                        )
            for p in self.json_args['points']:
                point = Points(x=p['x'],
                                y=p['y'],
                                message=p['message'],
                                radius=['radius'])
                event.points.append(point)
            self.session.add(event)
            self.session.commit()
            self.write_success()
        else:
            self.write_error('permission denied')


class ActivityDetailHandler(JSONHandler):
    
    pass

