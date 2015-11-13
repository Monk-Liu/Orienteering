define({ "api": [
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
            "description": "<p>出错信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response:",
          "content": "{\n    \"status\":2,\n    \"mesg\":\"用户没有登录，请登录/错误请求。。。\"\n}",
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
            "description": "<p>出错信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response:",
          "content": "{\n    \"status\":2,\n    \"mesg\":\"用户没有登录，请登录/错误请求。。。\"\n}",
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
            "description": "<p>出错信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response:",
          "content": "{\n    \"status\":2,\n    \"mesg\":\"用户没有登录，请登录/错误请求。。。\"\n}",
          "type": "json"
        }
      ]
    }
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
    "url": "/activity/:id",
    "title": "活动具体信息",
    "name": "________",
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
          },
          {
            "group": "Success 200",
            "type": "<p>Object</p> ",
            "optional": false,
            "field": "data",
            "description": "<p>包括每个点的信息</p> "
          }
        ]
      },
      "examples": [
        {
          "title": "Response 200 :",
          "content": "{\n    \"status\":1,\n    \"data\":[{},{},{}...]\n    //data 里面每个元素 都是 {\"position\":(111,40),\"task\":\"XXXXXXXX\"} 的形式\n}",
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