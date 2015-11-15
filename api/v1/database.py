from config import SQLINFO
import sqlalchemy
from sqlalchemy import Column,Integer,String,Text,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
from sqlalchemy.schema import Table,ForeignKey
import redis
import uuid




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
        self.phone = phone
        self.id = str(uuid.uuid4())
        self.password = ''

    def __repr__(self):
        return "<User (name='%s',id='%s')"%(self.name,self.id)


class UserInfo(Base):
    __tablename__ = 'userinfo'

    id = Column(Integer,primary_key=True)
    nickname = Column(String(60))
    #so what the lambda used for? http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#one-to-one
    event_id = relationship('Event',
                              secondary=lambda:UserEventTable, 
                              backref='participator',
                              passive_deletes = True
                              )

    def __init__(self,nickname):
        self.nickname = nickname
    
class Event(Base):
    __tablename__ = 'events'

    id = Column(String(50),primary_key=True)
    title = Column(Text)
    desc = Column(Text)  
    date = Column(DateTime)
    eventdetail = relationship("EventDetail",uselist=False,backref="event")
    userinfo_id = relationship(
            'UserInfo',
            secondary=lambda:UserEventTable,
            backref = 'the_event',
            passive_deletes = True
        )

    def __init__(self,title,desc,date):
        self.title = title
        self.desc = desc
        self.data = date

    def __repr__(self):
        return "<Event (id='%s',title='%s')"%(self.id,self.title)


class EventDetail(Base):
    __tablename__ = 'eventdetail'

    id = Column(Integer,primary_key=True)
    event_id = Column(String(50),ForeignKey('events.id'))
    

UserEventTable = Table('user_event',Base.metadata,
    Column('user_id',Integer,ForeignKey('userinfo.id')),
    Column('event_id',String(50),ForeignKey('events.id'))
    )

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
