# -*- coding:utf-8 -*-
"""
作者：张以白(Company)
日期：2023年02月03日
yaml导学: 基本操作-----读取文件----封装----读取配置文件

1 创建yaml格式文件
2 读取文件
3 输出文件
"""
# 读取单个文档
# 1 导入yaml包
import yaml
# with open("./data.yml","r",encoding="utf-8")as  f:
# # 2 yaml读取单个文档  yaml.safe_load()
#     r=yaml.safe_load(f)
# print(r)

# 2 yaml读取多个文档 yaml.safe_load_all()
# 1.导包
import yaml
from utils.YamlUtil import YamlReader

#
# # 2.yaml读取多个文档
# with open("data.yml", "r", encoding="utf-8") as f:
#     r = yaml.safe_load_all(f)
#     for i in r:
#         print(i)

# res = YamlReader("data.yml").data()
res = YamlReader("./data.yml").data_all()
print(res)
