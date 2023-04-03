# -*- coding:utf-8 -*-
"""
pytest函数级别的运行过程
作者：张以白(Company)
日期：2023年04月03日
"""
import pytest


# 1 定义类
class TestFunc:
    # 3 创建setup跟teardown
    def setup(self):
        print("这里是setup方法")
    def teardown(self):
        print("这里是teardown方法")
    # 2创建方法以test开头
    def test_a(self):
        print("test_a")
    def test_b(self):
        print("test_b")
# 4 运行查看结果
if __name__ == '__main__':
    pytest.main(["-s","pytest_func.py"])

    #函数级别方法：运行于方法始末，每次调用一次函数就会执行一次
    # 类级别方法: 运行于测试类的始末，一次测试只会调用一次setup和teardown方法，不关心有多少函数。
