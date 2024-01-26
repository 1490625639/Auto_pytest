# -*- coding: UTF-8 -*-
"""
Project ：Auto_pytestu 
File    ：test_GetHot.py
Author  ：张以白
Date    ：2024/1/26 1:39 
"""
import os
import pytest
import yaml

from utils.YamlUtil import YamlReader
from config import Conf
from config.Conf import ConfigYaml
from utils.RequesetsUtil import Request


class TestGetList:
    test_file = os.path.join(Conf.get_data_path(), "testgethot.yml")  # join用于拼接
    data_list = YamlReader(test_file).data_all()
    picture_file = os.path.join(Conf.get_data_path(), "picture_url.yml")

    @pytest.mark.parametrize("data", data_list)
    def test_gethot(self, data):
        url = ConfigYaml().get_conf_url() + data["url"]
        # print(url)
        res = Request().get(url)

        if data['expect_code'] == str(res['code']) and data['msg']:
            print(f"响应结果为：{res['code']}\n响应信息为：{res['body']['msg']}")
            for i in res['body']['result']:
                # print(i['picture'])
                with open(self.picture_file, 'a', encoding='utf-8') as file:
                    yaml.dump(i['picture'], file, default_flow_style=False, encoding='utf-8', allow_unicode=True)
        else:
            print("执行失败")


if __name__ == '__main__':
    pytest.main(["-s", "test_getlist.py"])
