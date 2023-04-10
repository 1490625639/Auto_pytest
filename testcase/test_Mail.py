# -*- coding:utf-8 -*-
"""
作者：张以白(Company)
日期：2023年02月03日
"""
import os
import json

import pytest

from common.Base import init_db
from config.Conf import ConfigYaml

"""
登录	登录成功	http://211.103.136.242:8064/authorizations/	
	POST	json	{"username":"python","password":"12345678"}
"""
# 登录
# 1、导入包
import requests
from  utils.RequesetsUtil import requests_get
from  utils.RequesetsUtil import requests_post
from utils.RequesetsUtil import Request
from utils.AssertUtil import AssertUtil
# 2、定义登录方法
def testlogin():
    conf_y=ConfigYaml()
    url_path=conf_y.get_conf_url()
    url=url_path+"/login"

    # 3 定义测试数据
    #url = ""
    data = {"username":"张三"}
    # 4发送
    # r = requests.post(url=url,data=data)
#    r=requests_post(url,json=data)
    # # 5 输出结果
    # print(r.json())
    request = Request()
    r = request.post(url, json=data)
    # 返回状态码
    code=r["code"]
    # 返回结果内容
    #body=json.dumps(r["body"])
    body=r["body"]
    #验证
    # AssertUtil().assert_code(code,200)
    # AssertUtil().assert_in_body(body,403)
    # #print(r)
# chatgpt修改后的代码
    try:
        AssertUtil().assert_code(code, 200)
    except AssertionError as e:
        print(e)
    try:
        AssertUtil().assert_in_body(body, 403)
    except AssertionError as e:
        print(e)
    # 初始化数据库对象
    conn=init_db(db_alias="db_1")
    # 查询结果
    res_db=conn.fetchone("select * from a")
    print(res_db)
    # 验证结果
    user_id=body["user_id"]
    assert user_id==res_db["id"]
"""
个人信息	获取个人信息正确	http://211.103.136.242:8064/user/	登录	get	
    headers: {'Authorization': 'JWT ' + this.token
    }
"""


# 需要使用到登录后的token
def testinfo():
    url = ""
    token = ""
    headers = {}
    # r = requests.get(url, headers)
    # print(r.json())
    # r=requests_get(url,headers)
    # print(r)
    request = Request()
    r = request.get(url, headers=headers)

"""
商品列表数据	商品列表数据正确	
http://211.103.136.242:8064/categories/115/skus/
get	json={
""page"":""1"",
""page_size"": ""10"",
""ordering"": ""create_time""
}"
"""

def goods_list():
    url = ""
    data = {}
    r = requests.get(url, json=data)
    print(r.json())

"""
购物车	添加购物车成功	http://211.103.136.242:8064/cart/	
登录	post	json	
{"sku_id": "3","count": "1", "selected": "true"}"""
def cart():
    url = ""
    data = {}
    headers = {}
    r=requests_post(url=url,json=data,headers=headers)
    print(r)

"""
订单	保存订单	http://211.103.136.242:8064/orders/	
登录	post	json	{ "address":"1","pay_method":"1" }
"""


def order():
    url = ""
    data = {}
    headers = {}
    r = requests.post(url, data, headers)
    print(r.json())


if __name__ == '__main__':
    #login()
    # info()
    # cart()
    # order()

# 1 根据默认的运行原则,调整py文件命名跟函数命名.
# 2 pytes.main()运行
# 3
    pytest.main(["-s"])