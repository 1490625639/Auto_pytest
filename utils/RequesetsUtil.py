# -*- coding:utf-8 -*-
"""
作者：张以白(Company)
日期：2023年02月03日
"""
import requests


# get方法的一个封装,将参数以及响应返回的json跟text做了判断
# 1创建一个封装的方法
def requests_get(url, headers):
    # 2 发送requests get请求
    r = requests.get(url, headers=headers)
    # 3获取结果响应内容
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    # 4 内容存放到字典中
    res = dict()
    res["code"] = code
    res["body"] = body

    # 5 字典返回
    return res


# post方法封装
# 1创建一个封装的方法    #由于json跟header可以不传,所以默认为None
def requests_post(url, json=None, headers=None):
# 2 发送post请求
    r = requests.post(url, json=json, headers=headers)
# 3获取结果响应内容
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:

        body = r.text
# 4 内容存放到字典中
    res=dict()
    res["code"]=code
    res["body"]=body

# 5 字典返回
    return  res
#---------------------以上为一种方法.但是比较复杂,需要重构

#重构
# 1 创建类
class Request:
# 2 定义公共方法
    #1.增加方法的参数,根据参数来验证方法get/post方法
    def requests_api(self,url=None,data=None,json=None,headers=None,cookies=None,method="get"):
        if method=="get":
            r = requests.get(url,data=data, json=json, headers=headers,cookies=cookies)
        elif  method=="post":
            r = requests.get(url,data=data, json=json, headers=headers,cookies=cookies)
    #2 重复的进行复制
        # 3获取结果响应内容
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:

            body = r.text
        # 4 内容存放到字典中
        res = dict()
        res["code"] = code
        res["body"] = body

        # 5 字典返回
        return res

# 3 重构get/post方法
    #get 1.定义方法
    def get(self,url,**kwargs):# 2.定义参数
        #3 调用公共方法
        return self.requests_api(url,method="get",**kwargs)
    def post(self,url,**kwargs):
        return  self.requests_api(url,method="post",**kwargs)