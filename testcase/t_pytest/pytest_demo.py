# -*- coding:utf-8 -*-
"""
作者：张以白(Company)
日期：2023年04月03日
"""
import pytest


# 创建一个方法
# 1 创建一个普通方法
def func(x):
    return x + 1
    # 2 创建一个pytest断言放啊


def test_a():
    print("这是test_a方法")
    assert func(3) == 5  # 断言失败


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_c():
    print("-----c-------")
    assert func(2) == 5


def test_b():
    print("这是我得test_b方法")
    assert 1  # 断言成功


# 使用pytest执行
# 1pycharm代码执行
if __name__ == '__main__':
    pytest.main(["-s", "pytest_demo.py"])
    # 2命令行执行
