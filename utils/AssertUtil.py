# -*- coding:utf-8 -*-
# 1 定义封装类
# 2 初始化数据,日志
# 3 code相等
# 4 body相等
# 5 body包含
import json


from utils.LogUtil import my_log
class AssertUtil:
    def __init__(self):
        self.log=my_log(AssertUtil)
    def assert_code(self,code,expected_code):
        try:
            assert int(code)==expected_code
            return True
        except:
            self.log.error("code error,当前code:%s,预期code为%s"%(code,expected_code))
            raise
    def assert_body(self,body,expected_body):
        try:
            assert body==expected_body
            return True
        except:
            self.log.error("body error,当前body:%s,预期body为%s"%(body,expected_body))
            raise
    def assert_in_body(self,body,expected_body):
        body=json.dumps(body)# 转义
        try:
            assert body in expected_body
            return True
        except:
            self.log.error("body error,当前body:%s,预期body为%s,二者不包含"%(body,expected_body))
            raise
