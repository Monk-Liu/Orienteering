define({ "api": [
  {
    "type": "post",
    "url": "/activity/add/",
    "title": "发起活动",
    "name": "AddActivity",
    "version": "0.2.0",
    "group": "Activities",
    "parameter": {
      "examples": [
        {
          "title": "Resquest-Example:",
          "content": "{\n    \"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\",\n    \"name\":\"华科僵尸跑\",\n    \"people_limit\":50,\n    \"start_time\":\"2015-11-12 00:00\",\n    \"during_time\":\"60\",\n    \"description\":\"xxxxxxxxxxxx\"\n    \"spotlist\":[{},{},{}...]，\n    \"loc_x\":10.0,\n    \"loc_y\":10.0,\n    \"loc_province\":\"湖北\",\n    \"loc_road\":\"xxx\",\n    \"loc_city\":\"xxx\",\n    //关于 spotlist 里面的{}\n    /*{ \"x\":120.00,\n        \"y\":40.00,\n       \"type\":1,\n       \"radius\":100,\n       \"message\":\"xxxxx\",\n       \"order\":1,\n      }*/\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Response 200:",
          "content": "{}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "Activities",
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "message",
            "description": "<p>出错信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"message\":\"错误信息（...）\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/activity/deletion/",
    "title": "删除活动",
    "name": "DelActivity",
    "version": "0.2.0",
    "group": "Activities",
    "permission": [
      {
        "name": "admin"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "key",
            "description": "<p>用户标识符.</p> "
          },
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "activity_id",
            "description": "<p>活动标识符.</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "\"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\",\n\"activity_id\":\"d5323e98-65f8-435b-a889-0c289f5835cb\"",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Response 200:",
          "content": "{}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "Activities",
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "message",
            "description": "<p>出错信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"message\":\"错误信息（...）\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/activity/list/",
    "title": "获得活动列表",
    "name": "____",
    "version": "0.2.0",
    "group": "Activities",
    "parameter": {
      "examples": [
        {
          "title": "Request-Example:",
          "content": "\"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\",  //这个感觉可有可无\n\"loc_x\":10.0,\n\"loc_y\":10.0,\n\"loc_province\":\"湖北\",\n\"loc_road\":\"xxx\",\n\"loc_city\":\"xxx\",\n\"page\":1,//分页的内容",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Response 200:",
          "content": "{\n    \"hot\":[{},{}...]\n    \"local\":[{},{}...]\n    /*{\n        \"name\":\"华科僵尸跑\",\n        \"id\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\",\n        \"people_limit\":50,\n        \"people_current\":20,\n        \"start_time\":\"2015-11-12 00:00\",\n        \"during_time\":\"60\"(分钟),\n        \"descriptioniption\":\"xxxxxxxxxxxx\"\n        \"spotlist\":[{},{},{}...]，\n        \"loc_x\":10.0,\n        \"loc_y\":10.0,\n        \"loc_province\":\"湖北\",\n        \"loc_road\":\"xxx\",\n        \"loc_city\":\"xxx\",\n    }*/\n    /*\n    {\n        \"name\":\"xxx\",\n        \"user_key\": \"1a941e54-e22e-4f36-bec7-a472e3ee87ff\",\n    }\n    */\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "Activities",
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "message",
            "description": "<p>出错信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"message\":\"错误信息（...）\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/activity/people/",
    "title": "参加活动的用户",
    "name": "_______",
    "version": "0.2.0",
    "group": "Activities",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "optional": false,
            "field": "acticity_id",
            "description": "<p>{String} 活动id</p> "
          }
        ]
      },
      "examples": [
        {
          "title": ":",
          "content": "\"activity_id\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\"",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Response 200:",
          "content": "{\n    \"people_list\":[{}...]\n    //{\n        \"name\":\"xxxx\",\n        \"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\"\n    }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"message\":\"xxxx\",\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "Activities"
  },
  {
    "type": "get",
    "url": "/activity/joined/",
    "title": "用户参加的活动",
    "name": "__________",
    "version": "0.2.0",
    "group": "Activities",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "optional": false,
            "field": "key",
            "description": "<p>{String} 用户标志符</p> "
          }
        ]
      },
      "examples": [
        {
          "title": ":",
          "content": "\"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\"",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Response 200:",
          "content": "{\n    \"acticity_list\":[{}...]\n    //活动细节看 活动列表\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"message\":\"xxxx\",\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "Activities"
  },
  {
    "type": "get",
    "url": "/activity/published/",
    "title": "用户发起的活动",
    "name": "__________",
    "version": "0.2.0",
    "group": "Activities",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "optional": false,
            "field": "key",
            "description": "<p>{String} 用户标识符</p> "
          }
        ]
      },
      "examples": [
        {
          "title": ":",
          "content": "\"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\"",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Response 200:",
          "content": "{\n    \"acticity_list\":[{}...]\n    //活动细节看 活动列表\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"message\":\"xxxx\",\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "Activities"
  },
  {
    "type": "post",
    "url": "/activity/attend/",
    "title": "加入活动",
    "name": "attend",
    "version": "0.2.0",
    "group": "Activities",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "key",
            "description": "<p>用户标识符.</p> "
          },
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "activity_id",
            "description": "<p>活动id.</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"activity_id\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\",\n    \"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\",\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Response 200:",
          "content": "{}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "message",
            "description": "<p>错误信息.</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"message\":\"xxxxx\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "Activities"
  },
  {
    "type": "get",
    "url": "/activity/finish/",
    "title": "新加的完成任务的接口",
    "name": "finish",
    "version": "0.2.0",
    "group": "Activities",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "optional": false,
            "field": "key",
            "description": "<p>用户标识符.</p> "
          },
          {
            "group": "Parameter",
            "optional": false,
            "field": "activity_id",
            "description": "<p>活动标识符.</p> "
          },
          {
            "group": "Parameter",
            "optional": false,
            "field": "finish_time",
            "description": "<p>完成时间.</p> "
          },
          {
            "group": "Parameter",
            "optional": false,
            "field": "spot_count",
            "description": "<p>到达点数.</p> "
          }
        ]
      },
      "examples": [
        {
          "title": ":",
          "content": "{\n    \"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\",\n    \"activities_id\":\"\",\n    \"finish_time\":\"2015-10-10 21:22;22\",\n    \"spots\":[{},{}...],\n    //spots 的形式参见 活动列表\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Response 200:",
          "content": "{}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"message\":\"xxxx\",\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "Activities"
  },
  {
    "type": "get",
    "url": "/city/",
    "title": "城市列表",
    "name": "CityList",
    "version": "0.2.0",
    "group": "Cities",
    "success": {
      "examples": [
        {
          "title": "Response 200:",
          "content": "{\n    \"citylist\":[{},{}...]\n        /* {}的具体格式\n        {\n            \"province_name\":\"xxx\",\n            \"cities\":[{\"code\":\"0001\",\"city\":\"city 1\"},\n                      {\"code\":\"0002\",\"city\":\"city 2\"},\n                      ...\n                     ]\n        }\n        */\n    }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "message",
            "description": "<p>错误信息.</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"message\":\"xxxxx\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "Cities"
  },
  {
    "type": "get",
    "url": "/splash/splash/",
    "title": "",
    "name": "splash",
    "version": "0.2.0",
    "group": "Splash",
    "success": {
      "examples": [
        {
          "title": "Response 200:",
          "content": "{\n    \"url\":\"xxxxxx\";\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "message",
            "description": "<p>错误信息.</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"message\":\"xxxxx\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "Splash"
  },
  {
    "type": "post",
    "url": "/users/",
    "title": "登录/注册",
    "name": "_____",
    "version": "0.2.0",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "phone",
            "description": "<p>手机号.</p> "
          },
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "password",
            "description": "<p>密码.</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "Base64({\n    \"phone\":\"15927278893\",\n    \"password\":\"admin\",\n    //关于加密的问题还是有可以改的地方的，这个还要商量（放到第二版？）\n})",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "key",
            "description": "<p>用户的key</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response (success) 200:",
          "content": "{\n    \"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "message",
            "description": "<p>错误信息.</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response (test) 400:",
          "content": "{\n    \"message\":\"错误信息(....)\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "User"
  },
  {
    "type": "get",
    "url": "/user/detail/:uid/",
    "title": "获取用户信息",
    "name": "______",
    "version": "0.2.0",
    "group": "User",
    "permission": [
      {
        "name": "none"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "key",
            "description": "<p>用户标识符key和url上的uid不同，uid表示表示被访问的用户，key代表自己.</p> "
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Response 200:",
          "content": "{\n    \"nickname\":\"panda\",\n    \"sex\":\"male\",\n    \"birthday\":\"2015-02-11\"\n    \"image\":\"http://run.monkliu.me:8888/static/1.jpg\",\n    \"event_attend\":[{},{},...],//{}内容参考 活动细节\n    \"event_launch\":[{},{},...],//同上\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "message",
            "description": "<p>错误信息.</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"message\":\"错误信息（...）\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "User"
  },
  {
    "type": "POST",
    "url": "/user/detail/:key/",
    "title": "修改用户信息",
    "name": "______",
    "version": "0.2.0",
    "group": "User",
    "permission": [
      {
        "name": "admin,本人"
      }
    ],
    "parameter": {
      "examples": [
        {
          "title": "Response:",
          "content": "{\n    \"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\",  \n    \"nickname\":\"panda\",\n    \"sex\":\"male\",\n    \"birthday\":\"2015-02-11\",\n    \"image\":\"http://run.monkliu.me:8888/staitc/1.jpg\"\n    //image 是客户端调用七牛后图片在七牛的url\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Response 200:",
          "content": "{}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "message",
            "description": "<p>错误信息.</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"message\":\"错误信息（用户不存在/权限不够）\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "User"
  },
  {
    "type": "get",
    "url": "/verify/",
    "title": "获取验证码",
    "name": "_____",
    "version": "0.2.0",
    "group": "Verify",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "phone",
            "description": "<p>手机号码.</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "\"phone\":Base64(\"15927278893\")",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Response (success) 200:",
          "content": "{}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "message",
            "description": "<p>错误信息.</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response (error) 400:",
          "content": "{\n    \"message\":\"错误信息（...）\",\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "Verify"
  },
  {
    "type": "post",
    "url": "/verify/",
    "title": "手机验证",
    "name": "_____",
    "version": "0.2.0",
    "group": "Verify",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "phone",
            "description": "<p>手机号码.</p> "
          },
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "password",
            "description": "<p>密码.</p> "
          },
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "verify",
            "description": "<p>验证码.</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "Base64({\n    \"phone\":\"15927278893\",\n    \"password\":\"admin\",\n    \"verify\":\"123456\",\n})",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "key",
            "description": "<p>用户标识符</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response (success) 200:",
          "content": "{\n    \"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\",\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Response (success) 400:",
          "content": "{\n    \"message\":\"错误信息（...）\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "Verify"
  }
] });