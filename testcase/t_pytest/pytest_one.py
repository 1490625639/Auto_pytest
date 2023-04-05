# -*- coding: utf-8 -*-
import pytest
"""
1 创建类和方法
    2 创建数据
    3 创建参数化
    4 运行
"""
# 1 创建类和方法
import pytest


class TestDemo:
    # 2 创建数据
    data_list=["xiaoming","xiaohong"]

    # 3 创建参数化
    @pytest.mark.parametrize("name",data_list)
    def test_a(self,name):
        print("test_a")
        print(name)
        assert  1

# 4 运行

if __name__ == '__main__':
    pytest.main(["./pytest.one.py"])