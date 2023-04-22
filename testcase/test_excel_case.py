import os
import json

import pytest

from common import Base
from common.ExcelData import Data
from config.Conf import ConfigYaml
from utils.LogUtil import my_log
from common import ExcelConfig
from utils.RequesetsUtil import Request

# 多个用例的
# 1 初始化用例文件
# ① 初始化用例文件
case_file = os.path.join("../data", ConfigYaml().get_excel_file())
# ② 获取用例sheet名称
sheet_name = ConfigYaml().get_excel_sheet()
# ③ 获取运行测试用例列表
data_init = Data(case_file, sheet_name)
run_list = data_init.get_run_data()

# ④ 日志
log = my_log()
# 初始化dataconfig
data_key = ExcelConfig.DataConfig


class TestExcel:
    def run_api(self,url,method,params=None,headers=None):
        # ② 发送请求API
        request = Request()
        # 验证params有没有内容
        if len(str(params).strip()) is not 0:
            # params转义成json
            params = json.loads(params)

        # get/post
        if str(method).lower() == "get":
            res = request.get(url, json=params, headers=headers)
        elif str(method).lower() == "post":
            res = request.post(url, json=params, headers=headers)
        else:
            log.error("这是一个错误请求:%s" % method)
        return res
    def run_pre(self, pre_case):
        url = ConfigYaml().get_conf_url() + pre_case[data_key.url]
        method = pre_case[data_key.method]
        params = pre_case[data_key.params]
        headers = pre_case[data_key.headers]
        # cookies = pre_case[data_key.cookies]
        header = Base.json_parse(headers)
        #cookie=Base.json_parse(cookies)
        res=self.run_api(url,method,params,headers)
        print("运行前置用例的结果为:",res)
    # ① 初始化信息
    # 1增加pytest方法
    @pytest.mark.parametrize("case", run_list)
    # 2 修改方法參數
    def test_run(self, case):
        #  print(data_key)
        # 3 重构函数内容
        url = ConfigYaml().get_conf_url() + case[data_key.url]
        """在run_list[0][data_key.url]中，run_list[0]表示取出运行测试用例列表中的第一条测试用例，data_key是一个常量类，里面定义了Excel表格中各列的列名，data_key.url表示取出该测试用例中名为“url”的一列的值。所以run_list[0][data_key.url]的含义是取出运行测试用例列表中第一条测试用例中的“url”这一列的值。"""
        # print(url)
        case_id = case[data_key.case_id]
        case_model = case[data_key.case_model]
        case_name = case[data_key.case_name]
        pre_exec = case[data_key.pre_exec]
        #  print(pre_exec)
        method = case[data_key.method]
        params = case[data_key.params]
        params_type = case[data_key.params_type]
        expect_result = case[data_key.expect_result]
        headers = case[data_key.headers]
        # cookies = case[data_key.cookies]
        code = case[data_key.code]
        db_verify = case[data_key.db_verify]
        # print(case_model,case_name,pre_exec,method,params,params_type,expect_result,headers,cookies,code,db_verify)

        if headers:  # 1 判断headers是否存在，json转义
            headers = json.loads(headers)
        else:
            headers = headers
        # if cookies:  # 1 判断cookies是否存在，json转义 2. 请求方法中增加headers,cookies 3 发送请求
        #     cookie = json.loads(cookies)
        # else:
        #     cookie = cookies
        # 1验证前置条件
        if pre_exec:
            pass
            # 2找到执行用例
            # 前置测试用例
            pre_case = data_init.get_case_pre(pre_exec)
            print("前置信息", pre_case)
            self.run_pre(pre_case)

# 2 测试用例方法,参数化运行

if __name__ == '__main__':
    # TestExcel.test_run()
    # 4 运行
    pytest.main(["-s", "test_excel_case.py"])

"""一个用例
# 1 初始化用例文件
# ① 初始化用例文件
case_file = os.path.join("../data", ConfigYaml().get_excel_file())
# ② 获取用例sheet名称
sheet_name = ConfigYaml().get_excel_sheet()
# ③ 获取运行测试用例列表
run_list = Data(case_file, sheet_name).get_run_data()
# ④ 日志
log = my_log()

class TestExcel:
    # ① 初始化信息
    def test_run(self):
        data_key = ExcelConfig.DataConfig
        url = ConfigYaml().get_conf_url() + run_list[0][data_key.url]
        在run_list[0][data_key.url]中，run_list[0]表示取出运行测试用例列表中的第一条测试用例，data_key是一个常量类，里面定义了Excel表格中各列的列名，data_key.url表示取出该测试用例中名为“url”的一列的值。所以run_list[0][data_key.url]的含义是取出运行测试用例列表中第一条测试用例中的“url”这一列的值。
        print(url)
        case_id = run_list[0][data_key.case_id]
        case_model = run_list[0][data_key.case_model]
        case_name = run_list[0][data_key.case_name]
        pre_exec = run_list[0][data_key.pre_exec]
        method = run_list[0][data_key.method]
        params = run_list[0][data_key.params]
        params_type = run_list[0][data_key.params_type]
        expect_result = run_list[0][data_key.expect_result]
        headers = run_list[0][data_key.headers]
        cookies = run_list[0][data_key.cookies]
        code = run_list[0][data_key.code]
        db_verify = run_list[0][data_key.db_verify]
        #print(case_model,case_name,pre_exec,method,params,params_type,expect_result,headers,cookies,code,db_verify)

        # ② 发送请求
        request = Request()
        # 验证params有没有内容
        if len(str(params).strip()) is not 0:
            # params转义成json
            params = json.loads(params)
        # get/post
        if str(method).lower() == "get":
            res = request.get(url, json=params)
        elif str(method).lower() == "post":
            res = request.post(url, json=params)
        else:
            log.error("这是一个错误请求:%s"%method)
        print(res)
# 2 测试用例方法,参数化运行

if __name__ == '__main__':
    TestExcel.test_run()
"""
