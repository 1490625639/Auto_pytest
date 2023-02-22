# -*- coding:utf-8 -*-
"""
作者：张以白(Company)
日期：2023年02月06日
1 首先获取项目路径
    1.获取当前项目的绝对路径
    2、定义config目录的路径
    3.定义conf.yml文件路径
2 读取配置文件

"""
import os
from utils.YamlUtil import YamlReader
current=os.path.abspath(__file__)
#print(current)
BASE_DIR=os.path.dirname(os.path.dirname(current))
#print(BASE_DIR)

#定义config目录
_config_path=BASE_DIR+os.sep+"config"
# 定义conf.yml路径
_config_file=_config_path+os.sep+"conf.yml"

# 因为是私有方法,定义一个方法来进行访问
def get_config_path():
    return  _config_path
def get_config_file():
    #print(_config_file)
    return _config_file

# 读取配置文件
    # 创建类
class ConfigYaml:
    # 初始yaml读取配置文件
    def __init__(self):
        self.config=YamlReader(get_config_file()).data()
        #print(self.config)
    # 定义方法获取信息
    def get_conf_url(self):

        return  self.config["BASE"]["test"]["url"]
if __name__ == '__main__':
    conf_read=ConfigYaml()
    print(conf_read.get_conf_url())