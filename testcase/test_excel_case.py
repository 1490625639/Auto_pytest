import re
import os
import json
import allure
import pytest
from utils.AssertUtil import AssertUtil
from common import Base
from common.ExcelData import Data
from config.Conf import ConfigYaml
from utils.LogUtil import my_log
from common import ExcelConfig
from utils.RequesetsUtil import Request
from config import Conf
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
    def run_api(self, url, method, params=None, headers=None):
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
        # cookie=Base.json_parse(cookies)
        res = self.run_api(url, method, params, headers)
        print("运行前置用例的结果为:", res)
        return res
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


        # 1验证前置条件
        if pre_exec:
            pass
            # 2找到执行用例
            # 前置测试用例
            pre_case = data_init.get_case_pre(pre_exec)
            print("前置条件信息", pre_case)
            pre_res= self.run_pre(pre_case)
            #headers,cookies= self.get_correlation(headers,cookies,pre_res)
            headers = self.get_correlation(headers,pre_res)
        header = Base.json_parse(headers)
        res = self.run_api(url, method, params, headers)
        print("测试用例执行:", res)

        #断言验证
        assert_util=AssertUtil()
        assert_util.assert_code(int(["code"],int(code)))

        # 返回结果内容
        assert_util.assert_in_body(str(res["body"]),str(expect_result))
        # 数据库断言验证
            # 1初始化
        from common.Base import init_db
        # sql=init_db("db_1")
        #     # 2查询sql
        # db_res=sql.fetchone(db_verify)
        # log.debug("数据库查询结果:{}".format(str(db_res)))
        #     # 3 数据库结果与接口返回进行验证
        # #获取数据库结果的key
        # verify_list=list(dict(db_res).keys())
        # #根据key获取数据库结果,接口结果
        # for  line in  verify_list:
        #     res_line=res["body"][line]
        #     res_db_line=dict(db_res)[line]
        #     assert_util.assert_body(res_line,res_db_line)
        Base.assert_db("db_1",res["body"],db_verify)


        # cookie=Base.json_parse(cookies)
        # if headers:  # 1 判断headers是否存在，json转义
        #     headers = json.loads(headers)
        # else:
        #     headers = headers
        # if cookies:  # 1 判断cookies是否存在，json转义 2. 请求方法中增加headers,cookies 3 发送请求
        #     cookie = json.loads(cookies)
        # else:
        #     cookie = cookies

        # allure
        allure.dynamic.feature(sheet_name)# 一级标签
        allure.dynamic.story(case_model) # 二级标签:模块
        allure.dynamic.title(case_id+case_name) #标题
        desc="<font color='red'>请求URL:    </font> {} <Br/>"\
         "<font color='red'>请求类型:        </font> {} <Br/>"\
         "<font color='red'>期望结果:        </font> {} <Br/>"\
         "<font color='red'>实际结果:        </font> {} <Br/>"\
            .format(url,method,expect_result,res)# 格式化转成字符串并添加网页标签
        allure.dynamic.description(desc)# 描述



#    def get_correlation(self,headers,cookies,pre_res):
#为了保障程序运行去除cookies+pre_res
    def get_correlation(self, headers, pre_res):
        """前置条件结果
        关联
        :param headers:
        :param cookies:
        :param pre_res:
        :return:
        """
        # 验证是否有关联
        #headers_para,cookies_para=Base.params_find(headers,cookies)
        # 为了保障程序运行去除cookies
        headers_para= Base.params_find(headers)
        # 有关联,执行前置用例,
        if len(headers_para):
            #  headers_data=pre_res["body"][headers_para[0]]
            """因为根据环境原因(接口不通),运行到此处实际返回的body为空,导致:TypeError: string indices must be integers
            所以加一个判断------由chatgpt提供"""
            if pre_res["body"]:
                headers_data = pre_res["body"][headers_para[0]]
            else:
                print("这里错误了")
                headers_data = None  # 或者任何其他你希望的默认值

        # 结果替换
        headers=Base.res_sub(headers,headers_data)
        # if len(cookies_para):
        #     cookies_data=pre_res["body"][cookies_para[0]]
        # # 结果替换
        # cookies=Base.res_sub(cookies,cookies_data)
        """为了保障程序运行去除cookies"""
#        return  headers,cookies
        return  headers

# 2 测试用例方法,参数化运行

if __name__ == '__main__':
    # TestExcel.test_run()
    # 4 运行
    report_path=Conf.get_report_path()+os.sep+ "result"
    report_html_path=Conf.get_report_path()+os.sep+"html"

    #pytest.main(["-s", "test_excel_case.py","--allure"," ./report/result"])
    pytest.main(["-s", "test_excel_case.py", "--allure", report_path])
#    Base.allure_report("./report/result","./report/html")
    Base.allure_report(report_path, report_html_path)











    """token知识点"""
    # str1 = '{"Authorization": "JWT ${token}$"}'
    # if "${" in str1:
    #     print(str1)
    # pattern = re.compile('\${(.*)}\$')
    # re_res = pattern.findall(str1)
    # print(re_res[0])
    # token="123"
    # """re.sub()是Python中的一个正则表达式函数，用于在字符串中替换匹配正则表达式的内容。
    #         它的参数包括三个：
    #         pattern：用于匹配字符串的正则表达式。可以是一个字符串或者一个正则表达式对象。
    #         repl：用于替换匹配到的字符串。可以是一个字符串或一个函数。
    #         string：要进行查找和替换的字符串。通过正则的查询跟替换实现token"""
    # res=re.sub(pattern,token,str1)
    # print("替换后 的token",res)

