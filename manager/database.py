from config import SQLINFO
import sqlalchemy
from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
from sqlalchemy.schema import Table, ForeignKey
import redis
import uuid
from utils import encrytovalue

def RedisOne():
    return redis.Redis('localhost', 6379, 0)

def RedisTwo():
    return redis.Redis("localhost", 6379, 1)

engine = sqlalchemy.engine_from_config(SQLINFO)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(String(50), primary_key=True)
    phone = Column(String(20))
    password = Column(String(50))
    info = relationship("UserInfo", backref=backref("user",uselist=False))

    def __init__(self, phone=None, password=None, id=None):
        if not id:
            self.phone = str(phone)
            self.id = str(uuid.uuid4())
            self.password = encrytovalue(password)
        else:
            self.id = id

class OAuthor(Base):
    __tablename__ = "OAuthor"

    id = Column(String(50))
    openid = Column(String(70), primary_key=True)

    def __init__(self,openid):
        self.openid = id
        self.id = str(uuid.uuid4())

class UserInfo(Base):
    __tablename__ = "userinfo"

    id = Column(Integer, primary_key=True)
    user_id = Column(String(50),ForeignKey("users.id"))
    nickname = Column(String(60))
    img_url = Column(String(1000))
    birthday = Column(Integer)
    sex = Column(Integer)
    weight = Column(Integer)
    height = Column(Integer)
    area = Column(String(30))
    host_event = relationship("Event", backref="hoster", passive_deletes=True)
    join_event = relationship("Team", backref="captain",passive_deletes=True)

    def __init__(self, nickname="匿名", img_url="http://120.27.163.43:8001/static/common.jpg",sex=1, birthday='1996-06-19', height=170,weight=60, area=""):

        self.nickname = nickname
        self.img_url = img_url
        self.sex = sex
        self.birthday = birthday
        self.height = height
        self.weight = weight
        self.area = area


class Event(Base):
    __tablename__ = "events"

    id = Column(String(50),primary_key=True)
    title = Column(String(1000))
    loc_x = Column(Float)
    loc_y = Column(Float)
    loc_province = Column(String(20))
    loc_distract = Column(String(1000))
    loc_city = Column(String(30))
    loc_road = Column(String(400))
    description = Column(Text)
    person_limit = Column(Integer)
    person_current = Column(Integer)
    person_per_team = Column(Integer)
    apply_start = Column(String(20))
    apply_end = Column(String(20))
    game_start = Column(String(20))
    game_end = Column(String(20))
    logo = Column(String(1000))
    type = Column(Integer) # 团体或个人
    prize = Column(String(1000))
    host = Column(Integer, ForeignKey("userinfo.id"))
    points = relationship("Points", backref="event",cascade="save-update,merge")#is that true?
    teams = relationship(
        "Team",
        backref = "event",
        passive_deletes = True
        )

    def __init__(self,title=None,desc=None,apply_start=None,
                apply_end=None,loc_x=None,loc_y=None,
                loc_province=None,person_limit=50,
                loc_distract=None,loc_road=None,loc_city=None,
                logo=None,host=None,type=0,game_start=None,
                game_end=None, team_contain=None,prize=None,
                slogan=None,person_per_team=None):
        self.id = str(uuid.uuid4())
        self.title      = title
        self.desc       = desc
        self.apply_start = apply_start
        self.apply_end = apply_end
        self.game_start = game_start
        self.game_end = game_end
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.loc_province = loc_province
        self.loc_road = loc_road
        self.loc_distract = loc_distract
        self.loc_city = loc_city
        self.person_limit = person_limit
        self.logo = logo
        self.host = host
        self.type = type #0 for single 1 for team
        self.slogan = slogan
        self.team_contain  = team_contain
        self.prize = prize

class Points(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y = Column(Float)
    message = Column(String(1000))
    pwd = Column(String(30))
    radius = Column(Float)
    type = Column(Integer)
    event_id = Column(String(50),ForeignKey("events.id"))
    teamlist = relationship("PointToTeam",
                           backref="point",
                           passive_deletes=True)

    def __init__(self,x=None,y=None,message=None,radius=None,type=1):
        self.x = x
        self.y = y
        self.radius = radius
        self.message = message
        self.type=type

class Team(Base):
    __tablename__ = "teams"

    #user_id, event_id, urgent_contact, urgent_phone, slogan, members

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("userinfo.id"))
    event_id = Column(String(50), ForeignKey("events.id"))
    name = Column(String(100))
    urgent_contact = Column(String(20))
    urgent_phone = Column(String(30))
    slogan = Column(String(1000))
    score = Column(Integer)
    check = Column(Integer)
    finish_points = Column(Integer)
    finish_time = Column(String(20))
    members = relationship("Members",
                          backref="team",
                          passive_deletes=True)
    pointlist = relationship("PointToTeam",
                            backref="team",
                            passive_deletes=True)

class Members(Base):
    __tablename__ = "Members"


    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    name = Column(String(20))
    idcard = Column(String(20))
    gender = Column(Integer)
    phone = Column(String(20))

class PointToTeam(Base):
    __tablename__ = "pointtoteam"

    point_id = Column(Integer, ForeignKey("points.id"),primary_key=True)
    team_id = Column(Integer, ForeignKey("teams.id"),primary_key=True)
    time = Column(String(30))

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

