""""""
@apiDefine MyError 

@apiError {String} mesg 出错信息
@apiErrorExample Response 400:
    {
        "mesg":"错误信息（...）"
    }
""""""
""""""
@apiDefine MySuccess

@apiSuccessExample Response 200:
    {}
""""""

""""""
@api {post} /users/ 登录/注册
@apiName 登录/注册
@apiVersion 0.2.0
@apiGroup User

@apiParam  {String} phone 手机号
@apiParam  {String} password 密码
@apiParamExample {json} Request-Example:
    Base64({
        "phone":"15927278893",
        "password":"admin",
        //关于加密的问题还是有可以改的地方的，这个还要商量（放到第二版？）
    })

@apiSuccess {String} key 用户的key
@apiSuccessExample Response (success) 200:
    {
        "key":"1a941e54-e22e-4f36-bec7-a472e3ee87ff"
    }

@apiError {String} mesg 错误信息
@apiErrorExample Response (test) 400:
    {
        "mesg":"错误信息(....)"
    }

""""""

""""""
@api {get} /verify/ 手机验证
@apiName 手机
@apiVersion 0.2.0
@apiGroup Verify

@apiParam {String} phone 手机号码
@apiParamExample {json} Request-Example:
    Base64({
        "phone":"15927278893"
    })

@apiSuccessExample Response (success) 200:
    {}

@apiError {String} mesg 错误信息
@apiErrorExample Response (success) 400:
    {
        "mesg":"错误信息（...）",
    }
""""""

""""""
@api {post} /verify/ 手机验证
@apiName 手机
@apiVersion 0.2.0
@apiGroup Verify

@apiParam {String} phone 手机号码
@apiParam {String} password 密码
@apiParam {String} verify 验证码
@apiParamExample {json} Request-Example:
    Base64({
        "phone":"15927278893",
        "password":"admin",
        "verify":"123456",
    })

@apiSuccess {String} key 用户标识符
@apiSuccessExample Response (success) 200:
    {
        "key":"1a941e54-e22e-4f36-bec7-a472e3ee87ff",
    }

@apiErrorExample Response (success) 400:
    {
        "mesg":"错误信息（...）"
    }
""""""

""""""
@api {get} /user/detail/:uid 获取用户信息
@apiGroup UserDetail
@apiName 获取用户信息
@apiVersion 0.2.0
@apiPermission none

@apiParam {String} key 用户标识符key和url上的uid不同，uid表示表示被访问的用户，key代表自己，

@apiSuccessExample Response 200:
    {
        "nickname":"panda",
        "sex":"male",
        "birthday":"2015-02-11"
        "image":"http://run.monkliu.me:8888/static/1.jpg",
        "event_attend":[{},{},...],//{}内容参考 活动细节
        "event_launch":[{},{},...],//同上
    }

@apiError {String} mesg 错误信息
@apiErrorExample Response 400:
    {
        "mesg":"错误信息（...）"
    }
""""""

""""""
@api {POST} /user/detail/:key 修改用户信息
@apiGroup UserInfo
@apiName 修改用户信息
@apiVersion 0.2.0
@apiPermission admin,本人

@apiParamExample Response:
    {
        "key":"1a941e54-e22e-4f36-bec7-a472e3ee87ff",  
        "nickname":"panda",
        "sex":"male",
        "birthday":"2015-02-11",
        "image":"http://run.monkliu.me:8888/staitc/1.jpg"
        //image 是客户端调用七牛后图片在七牛的url
    }


@apiSuccessExample Response 200:
    {}

@apiError {String} mesg 错误信息
@apiErrorExample Response 400:
    {
        "mesg":"错误信息（用户不存在/权限不够）"
    }
""""""


""""""
@api {get} /activities/ 获得活动列表
@apiName 活动列表
@apiVersion 0.2.0
@apiGroup Activities

@apiParamExample Request-Example:
    {
        "key":"1a941e54-e22e-4f36-bec7-a472e3ee87ff",  //这个感觉可有可无
        "loc_x":10.0,
        "loc_y":10.0,
        "loc_province":"湖北",
        "loc_road":"xxx",
        "loc_city":"xxx",
        "page":1,//分页的内容
    }

@apiSuccessExample Response 200:
    {
        "hot":[{},{}...]
        "local":[{},{}...]
        /*{
            "name":"华科僵尸跑",
            "id":"1a941e54-e22e-4f36-bec7-a472e3ee87ff",
            "people_limit":50,
            "people_current":20,
            "stime":"2015-11-12 00:00",
            "duringtime":"60"(分钟),
            "desc":"xxxxxxxxxxxx"
            "spotlist":[{},{},{}...]，
            "loc_x":10.0,
            "loc_y":10.0,
            "loc_province":"湖北",
            "loc_road":"xxx",
            "loc_city":"xxx",
        }*/
    }
@apiUse MyError

""""""

""""""
@api {post} /activities/ 发起活动
@apiName AddActivity
@apiVersion 0.2.0
@apiGroup Activities

@apiParamExample {json} Resquest-Example:
    {
        "key":"1a941e54-e22e-4f36-bec7-a472e3ee87ff",
        "name":"华科僵尸跑",
        "people_limit":50,
        "stime":"2015-11-12 00:00",
        "duringtime":"60",
        "desc":"xxxxxxxxxxxx"
        "spotlist":[{},{},{}...]，
        "loc_x":10.0,
        "loc_y":10.0,
        "loc_province":"湖北",
        "loc_road":"xxx",
        "loc_city":"xxx",
        //关于 spotlist 里面的{}
        /*{ "x":120.00,
            "y":40.00,
           "type":1,
           "radius":100,
           "message":"xxxxx",
          }*/
    }

@apiSuccessExample Response 200:
    {}
@apiUse MyError

""""""

""""""
@api {get} /activity/ 删除活动
@apiName DelActivity
@apiVersion 0.2.0
@apiGroup Activities
@apiPermission admin

@apiParam {String} key 用户标识符
@apiParam {String} id 活动标识符
@apiParamExample {json} Request-Example:
    {
        "key":"1a941e54-e22e-4f36-bec7-a472e3ee87ff",
        "id":"d5323e98-65f8-435b-a889-0c289f5835cb"
    }

@apiSuccessExample Response 200:
    {}
@apiUse MyError
""""""

    

""""""
@api {post} /activity/ 加入活动
@apiName 加入活动
@apiVersion 0.2.0
@apiGroup ActivityDetail

@apiParam {String} key 用户标识符
@apiParam {String} id 活动id
@apiParamExample Request-Example:
    {
        "id":"1a941e54-e22e-4f36-bec7-a472e3ee87ff",
        "key":"1a941e54-e22e-4f36-bec7-a472e3ee87ff",
    }

@apiSuccessExample Response 200:
    {}

@apiError {String} mesg 错误信息
@apiErrorExample Response 400:
    {
        "mesg":"xxxxx"
    }

""""""

""""""
@api {get} /city/ 城市列表
@apiName 城市列表
@apiVersion 0.2.0
@apiGroup Cities


@apiSuccessExample Response 200:
    {
        "citylist":[{},{}...]
            /* {}的具体格式
            {
                "province_name":"xxx",
                "cities":[{"code":"0001","city":"city 1"},
                          {"code":"0002","city":"city 2"},
                          ...
                         ]
            }
            */
        }
    }

@apiError {String} mesg 错误信息
@apiErrorExample Response 400:
    {
        "mesg":"xxxxx"
    }

""""""

""""""
@api {get} /splash/ splash
@apiName splash
@apiVersion 0.2.0
@apiGroup Splash


@apiSuccessExample Response 200:
    {
        "url":"xxxxxx";
    }

@apiError {String} mesg 错误信息
@apiErrorExample Response 400:
    {
        "mesg":"xxxxx"
    }

""""""
