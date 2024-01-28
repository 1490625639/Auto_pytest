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
    test_file = os.path.join(Conf.get_data_path(), "testgethotbrand.yml")  # join用于拼接
    data_list = YamlReader(test_file).data_all()

    @pytest.mark.parametrize("data", data_list)
    def test_gethot(self, data):
        url = ConfigYaml().get_conf_url() + data["url"]
        res = Request().get(url)
        # print(res)
        assert res['body']['code'] == data['expect_code']
        assert res["body"]['msg'] == data['msg']



if __name__ == '__main__':
    pytest.main(["-s", "test_getlist.py"])
