# -*- coding:utf-8 -*-
"""
作者：张以白(Company)
日期：2023年02月03日
Yaml封装
"""
import os
import yaml
# 1 创建类
class YamlReader:
    # 2 初始化,文件是否存在
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileExistsError("文件不存在")
        self._data = None
        self._data_all=None

    # 3 yaml读取
        #单个文档读取
    def data(self):

        if not self._data:
            with open(self.yamlf, "rb") as f:
                self._data= yaml.safe_load(f)
        return self._data
        #多个文档读取
    def data_all(self):

        if not self._data_all:
            with open(self.yamlf, "rb") as f:
                self._data_all= list(yaml.safe_load_all(f))
        return self._data_all