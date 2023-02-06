# -*- coding:utf-8 -*-
"""
作者：张以白(Company)
日期：2023年02月03日
"""
import os
import json
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
# 2、定义登录方法
def login():
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
    print(r)


"""
个人信息	获取个人信息正确	http://211.103.136.242:8064/user/	登录	get	
    headers: {'Authorization': 'JWT ' + this.token
    }
"""


# 需要使用到登录后的token
def info():
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
    # r = requests.post(url, json=data, headers=headers)
    # print(r.json())
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
    login()
    # info()
    # cart()
    # order()
