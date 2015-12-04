define({ "api": [
  {
    "type": "post",
    "url": "/activities/",
    "title": "发起活动",
    "name": "AddActivity",
    "version": "0.2.0",
    "group": "Activities",
    "parameter": {
      "examples": [
        {
          "title": "Resquest-Example:",
          "content": "{\n    \"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\",\n    \"name\":\"华科僵尸跑\",\n    \"people_limit\":50,\n    \"stime\":\"2015-11-12 00:00\",\n    \"duringtime\":\"60\",\n    \"desc\":\"xxxxxxxxxxxx\"\n    \"spotlist\":[{},{},{}...]，\n    \"loc_x\":10.0,\n    \"loc_y\":10.0,\n    \"loc_province\":\"湖北\",\n    \"loc_road\":\"xxx\",\n    \"loc_city\":\"xxx\",\n    //关于 spotlist 里面的{}\n    /*{ \"x\":120.00,\n        \"y\":40.00,\n       \"type\":1,\n       \"radius\":100,\n       \"message\":\"xxxxx\",\n      }*/\n}",
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
            "field": "mesg",
            "description": "<p>出错信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"mesg\":\"错误信息（...）\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "post",
    "url": "/activities",
    "title": "发起活动",
    "name": "AddActivity",
    "version": "0.1.0",
    "group": "Activities",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "name",
            "description": "<p>活动名称</p> "
          },
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "position",
            "description": "<p>活动地点</p> "
          },
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "time",
            "description": "<p>活动时间</p> "
          },
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "desc",
            "description": "<p>活动描述</p> "
          },
          {
            "group": "Parameter",
            "type": "<p>Object</p> ",
            "optional": false,
            "field": "spotlist",
            "description": "<p>活动的每一个点</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Resquest-Example:",
          "content": "{\n    \"name\":\"华科僵尸跑\",\n    \"position\":\"\",\n    \"time\":\"2015-11-12 00:00:00\",//这个也要约个格式\n    \"desc\":\"xxxxxxxxxxxx\"\n    \"spotlist\":[{},{},{}...]\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "<p>Number</p> ",
            "optional": false,
            "field": "status",
            "description": "<p>1</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response:",
          "content": "{\n    \"status\":1\n}",
          "type": "json"
        },
        {
          "title": "Response:",
          "content": "{\n    \"status\":1\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api.py",
    "groupTitle": "Activities",
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "mesg",
            "description": "<p>出错信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"mesg\":\"错误信息（...）\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/activity/",
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
            "description": "<p>用户标识符</p> "
          },
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "activity-id",
            "description": "<p>活动标识符</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\",\n    \"activity-id\":\"d5323e98-65f8-435b-a889-0c289f5835cb\"\n}",
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
            "field": "mesg",
            "description": "<p>出错信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"mesg\":\"错误信息（...）\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "delete",
    "url": "/activities/",
    "title": "删除活动",
    "name": "DelActivity",
    "version": "0.1.0",
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
            "description": "<p>用户标识符</p> "
          },
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "activity-id",
            "description": "<p>活动标识符</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\",\n    \"activity-id\":\"d5323e98-65f8-435b-a889-0c289f5835cb\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "<p>Number</p> ",
            "optional": false,
            "field": "status",
            "description": "<p>1</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response:",
          "content": "{\n    \"status\":1\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api.py",
    "groupTitle": "Activities",
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "mesg",
            "description": "<p>出错信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"mesg\":\"错误信息（...）\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/activities/",
    "title": "获得活动列表",
    "name": "____",
    "version": "0.2.0",
    "group": "Activities",
    "parameter": {
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\",  //这个感觉可有可无\n    \"loc_x\":10.0,\n    \"loc_y\":10.0,\n    \"loc_province\":\"湖北\",\n    \"loc_road\":\"xxx\",\n    \"loc_city\":\"xxx\",\n    \"page\":1,//分页的内容\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Response 200:",
          "content": "{\n    \"hot\":[{},{}...]\n    \"local\":[{},{}...]\n    /*{\n        \"name\":\"华科僵尸跑\",\n        \"people_limit\":50,\n        \"people_current\":20,\n        \"stime\":\"2015-11-12 00:00\",\n        \"duringtime\":\"60\"(分钟),\n        \"desc\":\"xxxxxxxxxxxx\"\n        \"spotlist\":[{},{},{}...]，\n        \"loc_x\":10.0,\n        \"loc_y\":10.0,\n        \"loc_province\":\"湖北\",\n        \"loc_road\":\"xxx\",\n        \"loc_city\":\"xxx\",\n    }*/\n}",
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
            "field": "mesg",
            "description": "<p>出错信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"mesg\":\"错误信息（...）\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/activities/",
    "title": "获得活动列表",
    "name": "____",
    "version": "0.1.0",
    "group": "Activities",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "key",
            "description": "<p>用户识别符</p> "
          },
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "position",
            "description": "<p>用来识别地理位置的参数，省份/城市/ 经纬度</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\",  //这个感觉可有可无\n    \"position\":\"武汉/湖北/ （120,80）\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "<p>Number</p> ",
            "optional": false,
            "field": "status",
            "description": "<p>成功返回 1</p> "
          },
          {
            "group": "Success 200",
            "type": "<p>Object</p> ",
            "optional": false,
            "field": "data",
            "description": "<p>活动的列表</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response:",
          "content": "{\n    \"status\":1,\n    \"data\":[{},{},{}]\n    //data 里面每个元素 都是 {\"position\":(111,40),\"task\":\"XXXXXXXX\"} 的形式\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api.py",
    "groupTitle": "Activities",
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "mesg",
            "description": "<p>出错信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"mesg\":\"错误信息（...）\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "post",
    "url": "/activity/:activity-id",
    "title": "加入活动",
    "name": "____",
    "version": "0.2.0",
    "group": "ActivityDetail",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "key",
            "description": "<p>用户标识符</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\",\n}",
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
            "field": "mesg",
            "description": "<p>错误信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"mesg\":\"xxxxx\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "ActivityDetail"
  },
  {
    "type": "post",
    "url": "/activity/",
    "title": "加入活动",
    "name": "____",
    "version": "0.1.0",
    "group": "ActivityDetail",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "key",
            "description": "<p>用户标识符</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\",\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "<p>Number</p> ",
            "optional": false,
            "field": "status",
            "description": "<p>成功返回1</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 200:",
          "content": "{\n    \"status\":1\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "<p>Number</p> ",
            "optional": false,
            "field": "status",
            "description": "<p>失败返回 2</p> "
          },
          {
            "group": "Error 4xx",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "mesg",
            "description": "<p>错误信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response:",
          "content": "{\n    \"status\":2,\n    \"mesg\":\"xxxxx\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api.py",
    "groupTitle": "ActivityDetail"
  },
  {
    "type": "get",
    "url": "/city/",
    "title": "城市列表",
    "name": "____",
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
            "field": "mesg",
            "description": "<p>错误信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"mesg\":\"xxxxx\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "Cities"
  },
  {
    "type": "get",
    "url": "/splash/",
    "title": "splash",
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
            "field": "mesg",
            "description": "<p>错误信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"mesg\":\"xxxxx\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "Splash"
  },
  {
    "type": "get",
    "url": "/user/detail/:uid",
    "title": "获取用户信息",
    "group": "UserDetail",
    "name": "______",
    "version": "0.2.0",
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
            "description": "<p>用户标识符key和url上的uid不同，uid表示表示被访问的用户，key代表自己，</p> "
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
            "field": "mesg",
            "description": "<p>错误信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"mesg\":\"错误信息（...）\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "UserDetail"
  },
  {
    "type": "get",
    "url": "/user/detail/:key",
    "title": "获取用户信息",
    "group": "UserDetail",
    "name": "______",
    "version": "0.1.0",
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
            "description": "<p>用户标识符</p> "
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "<p>Number</p> ",
            "optional": false,
            "field": "status",
            "description": "<p>成功返回 1</p> "
          },
          {
            "group": "Success 200",
            "type": "<p>Object</p> ",
            "optional": false,
            "field": "data",
            "description": "<p>用户信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response:",
          "content": "{\n    \"status\":1,\n    \"data\":{\n        \"nickname\":\"panda\",\n        \"sex\":\"male\",\n        \"image\":\"http://run.monkliu.me:8888/static/1.jpg\"\n    }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "<p>Number</p> ",
            "optional": false,
            "field": "status",
            "description": "<p>出错返回 2</p> "
          },
          {
            "group": "Error 4xx",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "mesg",
            "description": "<p>错误信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response :",
          "content": "{\n    \"status\":2,\n    \"mesg\":\"用户不存在。。。\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api.py",
    "groupTitle": "UserDetail"
  },
  {
    "type": "POST",
    "url": "/user/detail/:key",
    "title": "修改用户信息",
    "group": "UserInfo",
    "name": "______",
    "version": "0.2.0",
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
            "field": "mesg",
            "description": "<p>错误信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 400:",
          "content": "{\n    \"mesg\":\"错误信息（用户不存在/权限不够）\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "UserInfo"
  },
  {
    "type": "PUT",
    "url": "/user/detail/:key",
    "title": "修改用户信息",
    "group": "UserInfo",
    "name": "______",
    "version": "0.1.0",
    "permission": [
      {
        "name": "admin,本人"
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
            "description": "<p>用户标识符</p> "
          },
          {
            "group": "Parameter",
            "type": "<p>Object</p> ",
            "optional": false,
            "field": "data",
            "description": "<p>用户信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response:",
          "content": "{\n    \"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\",  \n    \"data\":{\n        \"nickname\":\"panda\",\n        \"sex\":\"male\",\n        \"image\":\"http://run.monkliu.me:8888/staitc/1.jpg\"\n    }\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "<p>Number</p> ",
            "optional": false,
            "field": "status",
            "description": "<p>成功返回 1</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response:",
          "content": "{\n    \"status\":1\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "<p>Number</p> ",
            "optional": false,
            "field": "status",
            "description": "<p>出错返回 2</p> "
          },
          {
            "group": "Error 4xx",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "mesg",
            "description": "<p>错误信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response :",
          "content": "{\n    \"status\":2,\n    \"mesg\":\"用户不存在。。。/权限不够\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api.py",
    "groupTitle": "UserInfo"
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
            "description": "<p>手机号</p> "
          },
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "password",
            "description": "<p>密码</p> "
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
            "field": "mesg",
            "description": "<p>错误信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response (test) 400:",
          "content": "{\n    \"mesg\":\"错误信息(....)\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "User"
  },
  {
    "type": "post",
    "url": "/users/",
    "title": "登录/注册",
    "name": "_____",
    "version": "0.1.0",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "phone",
            "description": "<p>手机号</p> "
          },
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "verify",
            "description": "<p>验证码</p> "
          },
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "password",
            "description": "<p>密码</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"phone\":\"15927278893\",\n    \"verify\":\"Zh90\",\n    \"password\":\"admin\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "<p>Number</p> ",
            "optional": false,
            "field": "status",
            "description": "<p>返回状态 1</p> "
          },
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
          "title": "Response (success):",
          "content": "{\n    \"status\":1,\n    \"key\":\"1a941e54-e22e-4f36-bec7-a472e3ee87ff\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "<p>Number</p> ",
            "optional": false,
            "field": "status",
            "description": "<p>返回状态 2</p> "
          },
          {
            "group": "Error 4xx",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "mesg",
            "description": "<p>错误信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response (test):",
          "content": "{\n    \"status\":2,\n    \"mesg\":\"用户密码/或者验证码错误\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api.py",
    "groupTitle": "User"
  },
  {
    "type": "post",
    "url": "/verify/",
    "title": "手机验证",
    "name": "__",
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
            "description": "<p>手机号码</p> "
          },
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "password",
            "description": "<p>密码</p> "
          },
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "verify",
            "description": "<p>验证码</p> "
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
          "content": "{\n    \"mesg\":\"错误信息（...）\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api2.py",
    "groupTitle": "Verify"
  },
  {
    "type": "get",
    "url": "/verify/",
    "title": "手机验证",
    "name": "__",
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
            "description": "<p>手机号码</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "Base64({\n    \"phone\":\"15927278893\"\n})",
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
            "field": "mesg",
            "description": "<p>错误信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response (success) 400:",
          "content": "{\n    \"mesg\":\"错误信息（...）\",\n}",
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
    "name": "__",
    "version": "0.1.0",
    "group": "Verify",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "phone",
            "description": "<p>手机号码</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"phone\":\"15927278893\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "<p>Number</p> ",
            "optional": false,
            "field": "status",
            "description": "<p>成功返回 1</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response (success):",
          "content": "{\n    \"status\":1\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "<p>Number</p> ",
            "optional": false,
            "field": "status",
            "description": "<p>失败返回 2</p> "
          },
          {
            "group": "Error 4xx",
            "type": "<p>String</p> ",
            "optional": false,
            "field": "mesg",
            "description": "<p>错误信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response (success):",
          "content": "{\n    \"status\":2,\n    \"mesg\":\"请不要频繁请求\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/api.py",
    "groupTitle": "Verify"
  }
] });