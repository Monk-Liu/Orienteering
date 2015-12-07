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
    return redis.Redis('localhost',6379,0)




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
class User(Base):
    __tablename__ = 'users'

    id = Column(String(50),primary_key=True)
    phone = Column(String(20))
    password = Column(String(50))
    info = relationship('UserInfo',backref=backref('user',uselist=False))

    def __init__(self,phone,password):
        self.phone = str(phone)
        self.id = str(uuid.uuid4())
        self.password = encrytovalue(password)

    def __repr__(self):
        return "<User (phone='%s',id='%s')"%(self.phone,self.id)


class UserInfo(Base):
    __tablename__ = 'userinfo'

    id = Column(Integer,primary_key=True)
    user_id = Column(String(50),ForeignKey('users.id'))
    nickname = Column(String(60))
    img_url = Column(String(3000))
    #img_url 没有做短url的必要吗？
    age = Column(Integer)
    sex = Column(Integer)
    #so what the lambda used for? http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#one-to-one
    join_event = relationship('Event',
                              secondary=lambda:UserEventTable, 
                              backref='participator',
                              passive_deletes = True
                              )
    host_event = relationship('Event',backref='hoster',passive_deletes=True)

    def __init__(self,nickname='匿名',img_url='/static/common.jpg',sex=1,age=20):
        self.nickname = nickname
        self.img_url = img_url
        self.sex = sex
        self.age = age

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
    loc_city = Column(Integer)
    loc_road = Column(String(400))
    desc = Column(Text)  
    people_limit = Column(Integer)
    people_current= Column(Integer)
    date = Column(DateTime)
    duringtime = Column(Integer)
    type = Column(Integer) 
    logo = Column(String(3000))
    host = Column(Integer,ForeignKey('userinfo.id'))
    eventdetail = relationship("EventDetail",uselist=False,backref="detail_event")
    points = relationship("Points",backref='point_event',cascade='save-update,merge,delete')
    userinfo_id = relationship(
            'UserInfo',
            secondary=lambda:UserEventTable,
            backref = 'the_event',
            passive_deletes = True
        )

    def __init__(self,title=None,desc=None,date=None,duringtime=60,
        loc_x=None,loc_y=None,loc_province=None,people_limit=50,
        loc_distract=None,loc_road=None,loc_city=None,logo=None,host=None):
        self.title = title
        self.desc = desc
        self.date = date
        self.duringtime = duringtime
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.loc_province = loc_province
        self.loc_road = loc_road
        self.loc_distract = loc_distract
        self.loc_city = loc_city
        self.people_limit = people_limit
        self.people_current = 1
        self.logo = logo
        self.host = host 

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
    event_re = Column(String(50),ForeignKey('events.id'))

    def __init__(self,x=None,y=None,message=None,radius=None,type=1):
        self.x = x
        self.y = y
        self.radius = radius
        self.message = message
        self.type=type

class EventDetail(Base):
    __tablename__ = 'eventdetail'

    id = Column(Integer,primary_key=True)
    event_re = Column(String(50),ForeignKey('events.id'))
    

UserEventTable = Table('user_event',Base.metadata,
    Column('user_id',Integer,ForeignKey('userinfo.id')),
    Column('event_id',String(50),ForeignKey('events.id'))
    )

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
