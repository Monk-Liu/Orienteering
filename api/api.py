""""""
@apiDefine MyError 

@apiError {Number} status 出错返回 2
@apiError {String} mesg 出错信息
@apiErrorExample Response:
    {
        "status":2,
        "mesg":"用户没有登录，请登录/错误请求。。。"
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
@apiVersion 0.1.0
@apiGroup User

@apiParam  {String} phone 手机号
@apiParam  {String} verify 验证码
@apiParam  {String} password 密码
@apiParamExample {json} Request-Example:
    {
        "phone":"15927278893",
        "verify":"Zh90",
        "password":"admin"
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
        "mesg":"用户密码/或者验证码错误"
    }

""""""

""""""
@api {post} /verify/ 手机验证
@apiName 手机
@apiVersion 0.1.0
@apiGroup Verify

@apiParam {String} phone 手机号码
@apiParamExample {json} Request-Example:
    {
        "phone":"15927278893"
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
        "mesg":"请不要频繁请求"
    }
""""""

""""""
@api {get} /user/detail/:key 获取用户信息
@apiGroup UserDetail
@apiName 获取用户信息
@apiVersion 0.1.0
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
            ...
        }
    }

@apiError {Number} status 出错返回 2
@apiError {String} mesg 错误信息
@apiErrorExample Response :
    {
        "status":2,
        "mesg":"用户不存在。。。"
    }
""""""

""""""
@api {PUT} /user/detail/:key 修改用户信息
@apiGroup UserInfo
@apiName 修改用户信息
@apiVersion 0.1.0
@apiPermission admin,本人

@apiParam {String} key 用户标识符
@apiParam {Object} data 用户信息
@apiParamExample Response:
    {
        "key":"1a941e54-e22e-4f36-bec7-a472e3ee87ff",  
        "data":{
            "nickname":"panda",
            "sex":"male",
            ...
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
        "mesg":"用户不存在。。。/权限不够"
    }
""""""


""""""
@api {get} /activities/ 获得活动列表
@apiName 活动列表
@apiVersion 0.1.0
@apiGroup Activities

@apiParam {String} key 用户识别符
@apiParam {String} position 用来识别地理位置的参数，省份/城市/ 经纬度
@apiParamExample Request-Example:
    {
        "key":"1a941e54-e22e-4f36-bec7-a472e3ee87ff",  //这个感觉可有可无
        "position":"武汉/湖北/ （120,80）"
    }

@apiSuccess {Number} status 成功返回 1
@apiSuccess {Object} data 活动的列表
@apiSuccessExample Response:
    {
        "status":1,
        "data":[{},{},{}]
        //data 里面每个元素 都是 {"postion":(111,40),"task":"XXXXXXXX"} 的形式
    }
@apiUse MyError

""""""

""""""
@api {post} /activities 发起活动
@apiName AddActivity
@apiVersion 0.1.0
@apiGroup Activities

@apiParam {String} name 活动名称
@apiParam {String} position 活动地点
@apiParam {String} time 活动时间
@apiParam {String} desc 活动描述
@apiParam {Object} spotlist 活动的每一个点
@apiParamExample {json} Resquest-Example:
    {
        "name":"华科僵尸跑",
        "position":"",
        "time":"2015-11-12 00:00:00",//这个也要约个格式
        "desc":"xxxxxxxxxxxx"
        "spotlist":[{},{},{}...]
    }

@apiSuccess {Number} status 1
@apiSuccessExample Response:
    {
        "status":1
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
@apiVersion 0.1.0
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
@api {get} /activity/:id 活动具体信息
@apiName 活动信息（具体）
@apiVersion 0.1.0
@apiGroup ActivityDetail

@apiParam {String} key 用户标识符
@apiParamExample Request-Example:
    {
        "key":"1a941e54-e22e-4f36-bec7-a472e3ee87ff",
    }

@apiSuccess {Number} status 成功返回1
@apiSuccess {Object} data 包括每个点的信息
@apiSuccessExample Response 200 :
    {
        "status":1,
        "data":[{},{},{}...]
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
@api {post} /activity/ 加入活动
@apiName 加入活动
@apiVersion 0.1.0
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
