import tornado.web
from tornado import gen
import database as DB
from database import Event,Team, Members, Points, PointToTeam,User

class BaseHandler(tornado.web.RequestHandler):
    
    def initialize(self):
        self.session = DB.Session()
    
    def on_finish(self):
        self.session.commit()
        self.session.close()

    def get_current_user(self):
        return self.get_secure_cookie("user")

class LoginHandler(BaseHandler):

    def checkuser(self, username, password):
        if username=="qudong" and password == "qudong":
            return True
        return False

    def get(self):
        self.render("login.html", error=None)

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        if self.checkuser(username, password):
            self.set_secure_cookie('user',username)
            self.redirect("/show/events/")
        else:
            self.render("login.html", error="username or password not correct")

class ShowEventHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        page = self.get_argument('page','')
        province = self.get_argument('province','')
        if page:
            try:
                page = int(page)
                page = page-1 if page else page
            except:
                page = 0
        else:
            page = 0
        if province:
            events = self.session.query(Event).offset(page*20).limit(20)
        else:
            events = self.session.query(Event).offset(page*20).limit(20)
        prepage = page-1 if page else None
        nextpage = page+1 if events.count() == 20 else None
        self.render('showevent.html',events=events, prepage=prepage, nextpage=nextpage)

    @tornado.web.authenticated
    def post(self):
        activity_id = self.get_argument('id','')
        if activity_id:
            event = self.session.query(Event).get(activity_id)
            if event:
                for team in event.teams:
                    for member in team.members:
                        self.session.delete(member)
                    self.session.commit()
                    self.session.delete(team)
                self.session.commit()
                for point in event.points:
                    self.session.delete(point)
                    self.session.commit()
                    self.session.delete(event)
                    self.session.commit()
        self.redirect('/show/events/')


class ShowUserHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        page = self.get_argument('page','')
        phone = self.get_argument("phone",'')
        if not phone:
            if page:
                try:
                    page = int(page)
                    page = page-1 if page else page
                except:
                    page = 0
            else:
                page = 0
            users = self.session.query(User).offset(page*20).limit(20)
        else:
            users = self.session.query(User).filter(User.phone==phone)
        for user in users:
            user.nickname = user.info[0].nickname
            user.sex = user.info[0].sex
        prepage = page-1 if page else None
        nextpage = page+1 if users.count() == 20 else None
        self.render('showuser.html',users=users, prepage=prepage, nextpage=nextpage)

    @tornado.web.authenticated
    def post(self):
        user_id = self.get_argument('key')
        if user_id:
            user = self.session.query(User).get(activity_id)
            if user:
                #the OAuthor
                self.session.delete(user.info)
                self.session.commit()
                self.session.delete(user)
                self.session.commit()
        self.redirect("/")

class EventByUserHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        type = self.get_argument('type', '')
        id = self.get_argument('id', '')
        if type and id:
            user = self.session.query(User).get(id)
            if user:
                if type== 'host':
                    events = user.info[0].host_event
                else:
                    events  = []
                    for e in  user.info[0].join_event:
                        events.append(e.event)
            else:
                events = []
            self.render('showevent.html', events=events, prepage=None, nextpage=None)
        else:
            self.redirect("/notfound")

class UserByEventHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        id = self.get_argument('id', '')
        if id:
            event = self.session.query(Event).get(id)
            if event:
                users = []
                if type=='host':
                    userinfo = event.hoster
                    user = userinfo.user
                    if user:
                        u  = {}
                        u['nickname'] = userinfo.nickname
                        u['id'] = userinfo.user_id
                        u['password'] = user.password
                        u['sex'] = userinfo.sex
                        u['phone'] = user.phone
                        users.append(u)
                    self.render('showuser.html', users=users, prepage=None, nextpage=None)
                else:
                    for team in event.teams:
                        t = {}
                        t['name'] = team.name
                        t['id'] = team.id
                        t['slogan'] = team.slogan
                        t['score'] = team.score
                        t['check'] = team.check
                        #t['event_id'] = team.event_id
                        #t['user_id'] = team.user_id
                        users.append(t)
                    self.render('showteam.html', teams=users, prepage=None, nextpage=None)
            else:
                users = []
                self.render('showuser.html', users=users, prepage=None, nextpage=None)
        else:
            self.redirect('/notfound')



#签到
class ActivityCheckHandler(BaseHandler):

    #显示 所有队伍签到信息
    @tornado.web.authenticated
    def get(self):
        event_id = self.get_argument("activity_id",'')
        if event_id:
            event = self.session.query(Event).get(event_id)
            teams = []
            for team in event.teams:
                t = {}
                t['name'] = team.name
                t['slogan'] = team.slogan
                t['id'] = team.id
                t['check'] = team.check
                t['score'] = team.score
                teams.append(t)
            self.render("showteam.html", teams=teams,prepage=None, nextpage=None)
        else:
            self.redirect("/notfound")


    #对某个队伍签到
    @tornado.web.authenticated
    def post(self):
        team_id = self.get_argument("team_id",'')
        if team_id :
            team = self.session.query(Team).get(team_id)
            if team:
                team.check = 1
                self.session.merge(team)
                self.session.commit()
                self.redirect("/show/events/")
            else:
                self.redirect("/teamfound")
        else:
            self.redirect("/notfound")

#显示队伍信息
class ActivityTeamHandler(BaseHandler):

    #显示队伍 完成时间， 队名。。。 分数
    @tornado.web.authenticated
    def get(self):
        team_id = self.get_argument("team_id")
        if team_id:
            team = self.session.query(Team).get(team_id)
            if team:
                t = {}
                t['id'] = team_id
                t['name'] = team.name
                t['slogan'] = team.slogan
                t['urgent_contact'] = team.urgent_contact
                t['urgent_phone'] = team.urgent_phone
                t['score'] = team.score
                t['check'] = team.check
                t['members'] = []
                for member in team.members:
                    m ={}
                    m['name'] = member.name
                    m['idcard'] = member.idcard
                    m['phone'] = member.phone
                    m['gender'] = member.gender
                    t['members'].append(m)
                t['points'] = []
                for point_re in team.pointlist:
                    point = point_re.point
                    p = {}
                    p['id'] = point.id
                    p['message'] = point.message
                    p['time'] = point_re.time
                    t['points'].append(p)
                self.render("teamdetail.html", team=t)
            else:
                self.redirect("/teamnot found")
        else:
            self.redirect("/not found")

    #修改分数
    @tornado.web.authenticated
    def post(self):
        team_id = self.get_argument("team_id",'')
        score = self.get_argument("score","")
        if score and team_id:
            team =self.session.query(Team).get(team_id)
            if team:
                team.score = score
                self.session.merge(team)
                self.session.commit()
                self.redirect("/show/activity/check/?activity_id="+team.event_id)
            else:
                self.write("Team not foun")
        else:
            self.write("arguments error")

#对应每个点的 pwd
class ActivityPointHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        event_id = self.get_argument("activity_id",'')
        if event_id:
            event = self.session.query(Event).get(event_id)
            pointlist = []
            for point in event.points:
                p = {}
                p['id'] = point.id
                p['x'] = point.x
                p['y'] = point.y
                p['pwd'] = point.pwd
                p['type'] = point.type
                p['radius'] = point.message
                pointlist.append(p)
            self.render("showpoints.html",points=pointlist)


    @tornado.web.authenticated
    def post(self):
        point_id = self.get_argument("id")
        pwd = self.get_argument("pwd")
        if point_id and pwd:
            point = self.session.query(Points).get(point_id)
            if point:
                point.pwd = pwd
                self.session.merge(point)
                self.session.commit()
                self.redirect("/show/points/?activity_id="+point.event_id)
            else:
                self.redirect("/pointnotfound")
        else:
            self.redirect("/notfound")

class DisclaimerHandler(BaseHandler):

    def get(self):
        self.redis = DB.RedisTwo()
        disclaimer = self.redis.get("disclaimer")
        self.render("disclaimer.html", disclaimer=disclaimer)

    def post(self):
        disclaimer = self.get_argument("disclaimer")
        if disclaimer:
            self.redis = DB.RedisTwo()
            self.redis.set("disclaimer",disclaimer)
        self.redirect("/change/disclaimer/")