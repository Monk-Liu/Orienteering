from config import SQLINFO
import sqlalchemy
from sqlalchemy import Column,Integer,String,Text,DateTime,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
from sqlalchemy.schema import Table,ForeignKey
import redis
import uuid
from utils import encrytovalue




def Redis():
    #return redis.Redis('localhost',6379,0)
    return

engine = sqlalchemy.engine_from_config(SQLINFO)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# two way to make one to one relationship backref or foreignkey
'''
ToDo:   1.set Column as unicode,text
        2.cascade : default is save-update merge 
                    other contain all,delte-orphan, 
                see:http://docs.sqlalchemy.org/en/latest/orm/cascades.html#backref-cascade
        3.passive_detele
        4.what's the difference between unicode and string

'''

class UserEvent(Base):
    __tablename__ = 'user_event'

    event_id = Column(String(50), ForeignKey('events.id'),primary_key=True)
    user_id  = Column(Integer, ForeignKey('userinfo.id'),primary_key=True)
    finish_time = Column(String(20))
    finish_points = Column(Integer) # 本来是要有 和point的对应关系的，但是可以用另一种、
    #更快的方法实现的， 主要是 类似 linux 权限管理的 1 4 7 那些数字一样的想法
    event = relationship("Event")
    parent = relationship("UserInfo")
    
    def __init__(self, finish_time='', finish_points=0):
        self.finish_time = finish_time
        self.finish_points = finish_points
    


class User(Base):
    __tablename__ = 'users'

    id = Column(String(50),primary_key=True)
    phone = Column(String(20))
    password = Column(String(50))
    info = relationship('UserInfo',backref=backref('user',uselist=False))

    def __init__(self,phone=None,password=None,id=None):
        if not id:
            self.phone = str(phone)
            self.id = str(uuid.uuid4())
            self.password = encrytovalue(password)
        else:
            self.id = id

    def __repr__(self):
        return "<User (phone='%s',id='%s')"%(self.phone,self.id)

class OAuthor(Base):
    __tablename__ = 'OAuthor'

    id = Column(String(50));
    openid = Column(String(70),primary_key=True)

    def __init__(self,id):
        self.openid = id
        self.id = str(uuid.uuid4())

class UserInfo(Base):
    __tablename__ = 'userinfo'

    id = Column(Integer,primary_key=True)
    user_id = Column(String(50),ForeignKey('users.id'))
    nickname = Column(String(60))
    img_url = Column(String(3000))
    #img_url 没有做短url的必要吗？
    birthday = Column(String(60))
    sex = Column(Integer)
    height = Column(Integer)
    weight = Column(Integer)
    area = Column(String(30))
    #so what the lambda used for? http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#one-to-one
    join_event = relationship('UserEvent',
                              backref='the_user',
                              passive_deletes = True
                              )
    host_event = relationship('Event',backref='hoster',passive_deletes=True)

    def __init__(self,nickname='匿名',img_url='http://120.27.163.43:8001/static/common.jpg',sex=1,birthday='1996-06-19',height=None,weight=None,area=""):
        self.nickname = nickname
        self.img_url = img_url
        self.sex = sex
        self.birthday = birthday
        self.area = area
        if height:
            self.height = height
        else:
            self.height = 170 if self.sex else 165
        self.weight = weight if weight else 60 if self.sex else 50

    '''
    def change_info(self,nickname,img_url,sex,age):
        self.nickname = nickname
        self.img_url = img_url
        self.sex = sex
        self.age = age
    '''

class Event(Base):
    __tablename__ = 'events'

    id = Column(String(50),primary_key=True)
    title = Column(Text)
    loc_x =  Column(Float)
    loc_y = Column(Float)
    loc_province = Column(String(20))
    loc_distract = Column(String(1000))
    loc_city = Column(String(30))
    loc_road = Column(String(400))
    desc = Column(Text)  
    person_limit = Column(Integer)
    person_current= Column(Integer)
    start_time = Column(String(20))
    during_time = Column(String(20))
    type = Column(Integer) 
    logo = Column(String(3000))
    host = Column(Integer,ForeignKey('userinfo.id'))
    points = relationship("Points",backref='point_event',cascade='save-update,merge,delete')
    userinfo_id = relationship(
            'UserEvent',
            backref = 'the_event',
            passive_deletes = True
        )

    def __init__(self,title=None,desc=None,start_time=None,
                 during_time=60,loc_x=None,loc_y=None,
                 loc_province=None,person_limit=50,
                c_distract=None,loc_road=None,loc_city=None,
                 logo=None,host=None,type=0):
        self.id = str(uuid.uuid4())
        self.title      = title
        self.desc       = desc
        self.start_time = start_time
        self.during_time= during_time
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.loc_province = loc_province
        self.loc_road = loc_road
        self.loc_distract = loc_distract
        self.loc_city = loc_city
        self.person_limit = person_limit
        self.person_current = 0
        self.logo = logo
        self.host = host 
        self.type = type

    def __repr__(self):
        return "<Event (id='%s',title='%s')"%(self.id,self.title)

class Points(Base):
    __tablename__ = 'points'

    id = Column(Integer,primary_key=True)
    x = Column(Float)
    y = Column(Float)
    message = Column(Text())
    radius = Column(Float)
    type = Column(Integer)
    order = Column(Integer)
    event_re = Column(String(50),ForeignKey('events.id'))

    def __init__(self,x=None,y=None,message=None,radius=None,order=None,type=1):
        self.x = x
        self.y = y
        self.order = order
        self.radius = radius
        self.message = message
        self.type=type
'''
class EventDetail(Base):
    __tablename__ = 'eventdetail'

    id = Column(Integer,primary_key=True)
    event_re = Column(String(50),ForeignKey('events.id'))
'''  



if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
