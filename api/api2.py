""""""
@apiDefine MyError 

@apiError {Number} status 出错返回 2
@apiError {String} mesg 出错信息
@apiErrorExample Response:
    {
        "status":2,
        "mesg":"错误信息（...）"
    }
""""""
""""""
@apiDefine MySuccess

@apiSuccess {Number} status 1
@apiSuccessExample Response:
    {
        "status":1
    }
""""""

""""""
@api {post} /users/ 登录/注册
@apiName 登录/注册
@apiVersion 0.2.0
@apiGroup User

@apiParam  {String} phone 手机号
@apiParam  {String} password 密码
@apiParamExample {json} Request-Example:
    {
        "phone":Base64("15927278893"),
        "password":Base64("admin"),
        //关于加密的问题还是有可以改的地方的，这个还要商量（放到第二版？）
    }

@apiSuccess {Number} status 返回状态 1
@apiSuccess {String} key 用户的key
@apiSuccessExample Response (success):
    {
        "status":1,
        "key":"1a941e54-e22e-4f36-bec7-a472e3ee87ff"
    }

@apiError {Number} status 返回状态 2
@apiError {String} mesg 错误信息
@apiErrorExample Response (test):
    {
        "status":2,
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
    {
        "phone":Base64("15927278893")
    }

@apiSuccess {Number} status 成功返回 1
@apiSuccessExample Response (success):
    {
        "status":1
    }

@apiError {Number} status 失败返回 2
@apiError {String} mesg 错误信息
@apiErrorExample Response (success):
    {
        "status":2,
        "mesg":"错误信息（...）"
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
    {
        "phone":Base64("15927278893"),
        "password":Base64("admin"),
        "verify":"123456",
    }

@apiSuccess {Number} status 成功返回 1
@apiSuccessExample Response (success):
    {
        "status":1,
        "data":{
            "key":"1a941e54-e22e-4f36-bec7-a472e3ee87ff",
        }
    }

@apiError {Number} status 失败返回 2
@apiError {String} mesg 错误信息
@apiErrorExample Response (success):
    {
        "status":2,
        "mesg":"错误信息（...）"
    }
""""""

""""""
@api {get} /user/detail/:uid 获取用户信息
@apiGroup UserDetail
@apiName 获取用户信息
@apiVersion 0.2.0
@apiPermission none

@apiParam {String} key 用户标识符

@apiSuccess {Number} status 成功返回 1
@apiSuccess {Object} data 用户信息
@apiSuccessExample Response:
    {
        "status":1,
        "data":{
            "nickname":"panda",
            "sex":"male",
            "birthday":"2015-02-11"
            "image":"http://run.monkliu.me:8888/static/1.jpg",
            "event_attend":[{},{},...],//{}内容参考 活动细节
            "event_launch":[{},{},...],//同上
        }
    }

@apiError {Number} status 出错返回 2
@apiError {String} mesg 错误信息
@apiErrorExample Response :
    {
        "status":2,
        "mesg":"错误信息（...）"
    }
""""""

""""""
@api {PUT} /user/detail/:key 修改用户信息
@apiGroup UserInfo
@apiName 修改用户信息
@apiVersion 0.2.0
@apiPermission admin,本人

@apiParam {String} key 用户标识符
@apiParam {Object} data 用户信息
@apiParamExample Response:
    {
        "key":"1a941e54-e22e-4f36-bec7-a472e3ee87ff",  
        "data":{
            "nickname":"panda",
            "sex":"male",
            "birthday":"2015-02-11",
            "image":"http://run.monkliu.me:8888/staitc/1.jpg"
        }
    }


@apiSuccess {Number} status 成功返回 1
@apiSuccessExample Response:
    {
        "status":1
    }

@apiError {Number} status 出错返回 2
@apiError {String} mesg 错误信息
@apiErrorExample Response :
    {
        "status":2,
        "mesg":"错误信息（用户不存在/权限不够）"
    }
""""""


""""""
@api {get} /activities/ 获得活动列表
@apiName 活动列表
@apiVersion 0.2.0
@apiGroup Activities

@apiParam {String} key 用户识别符
@apiParam {String} position 用来识别地理位置的参数，省份/城市/ 经纬度
@apiParamExample Request-Example:
    {
        "key":"1a941e54-e22e-4f36-bec7-a472e3ee87ff",  //这个感觉可有可无
        "data":{
            "loc_x":10.0,
            "loc_y":10.0,
            "loc_province":"湖北",
            "loc_road":"xxx",
            "loc_city":"xxx",
        }
    }

@apiSuccess {Number} status 成功返回 1
@apiSuccess {Object} data 活动的列表
@apiSuccessExample Response:
    {
        "status":1,
        "data":{
            "hot":[{},{}...]
            "local":[{},{}...]
        }
        /*{
            "name":"华科僵尸跑",
            "people_limit":50,
            "people_current":20,
            "time":"2015-11-12 00:00",
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
@api {post} /activities 发起活动
@apiName AddActivity
@apiVersion 0.2.0
@apiGroup Activities

@apiParam {String} name 活动名称
@apiParam {Object} data 具体的数据
@apiParamExample {json} Resquest-Example:
    {
        "key":"1a941e54-e22e-4f36-bec7-a472e3ee87ff",
        "data":{
            "name":"华科僵尸跑",
            "people_limit":50,
            "time":"2015-11-12 00:00",
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
    }

@apiSuccess {Number} status 1
@apiSuccessExample Response:
    {
        "status":1
    }
@apiUse MyError

""""""

""""""
@api {delete} /activities/ 删除活动
@apiName DelActivity
@apiVersion 0.2.0
@apiGroup Activities
@apiPermission admin

@apiParam {String} key 用户标识符
@apiParam {String} activity-id 活动标识符
@apiParamExample {json} Request-Example:
    {
        "key":"1a941e54-e22e-4f36-bec7-a472e3ee87ff",
        "activity-id":"d5323e98-65f8-435b-a889-0c289f5835cb"
    }

@apiSuccess {Number} status 1
@apiSuccessExample Response:
    {
        "status":1
    }
@apiUse MyError
""""""

    

""""""
@api {post} /activity/ 加入活动
@apiName 加入活动
@apiVersion 0.2.0
@apiGroup ActivityDetail

@apiParam {String} key 用户标识符
@apiParamExample Request-Example:
    {
        "key":"1a941e54-e22e-4f36-bec7-a472e3ee87ff",
    }

@apiSuccess {Number} status 成功返回1
@apiSuccessExample Response 200:
    {
        "status":1
    }

@apiError {Number} status 失败返回 2
@apiError {String} mesg 错误信息
@apiErrorExample Response:
    {
        "status":2,
        "mesg":"xxxxx"
    }

""""""

""""""
@api {get} /city/ 城市列表
@apiName 城市列表
@apiVersion 0.2.0
@apiGroup Cities

@apiParam {String} key 用户标识符
@apiParamExample Request-Example:
    {
        "key":"1a941e54-e22e-4f36-bec7-a472e3ee87ff",
    }

@apiSuccess {Number} status 成功返回1
@apiSuccess {Object} data 具体数据
@apiSuccessExample Response 200:
    {
        "status":1，
        "data":{
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
""""""
