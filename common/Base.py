import json
import re
import subprocess
from config.Conf import ConfigYaml
from utils.LogUtil import my_log
from utils.MysqlUtil import Mysql
from utils.AssertUtil import AssertUtil

p_data = '\${(.*)}\$'

log = my_log()


# 测试push时候是否需要进行登录
# 数据库的初始化  相当于将get_db_conf_info()中进行了封装.
# 1 定义init_db
def init_db(db_alias):
    # 2 初始化数据化信息,通过配置
    db_info = ConfigYaml().get_db_conf_info(db_alias)
    print(db_info)
    host = db_info["db_host"]
    user = db_info["db_user"]
    password = db_info["db_password"]
    db_name = db_info["db_name"]
    charset = db_info["db_charset"]
    port = int(db_info["db_port"])
    # 01点10分
    # 3 初始化mysql对象
    conn = Mysql(host, user, password, db_name, charset, port)
    print(conn)
    return conn


def json_parse(data):
    """格式化字符，转换成json格式"""
    return json.loads(data) if data else data


def res_find(data, pattern_data=p_data):  # pattern_data是一个默认参数
    """查询(正则),并给出了一个默认的条件"""
    # pattern = re.compile('\${(.*)}\$')
    """re.compile(ptaaern_data).findall(data)是使用正则表达式从文本中匹配出符合要求的字符串，具体解释如下：
re.compile(pattern_data)：将正则表达式pattern_data编译为一个正则表达式对象，以便重复使用，避免多次编译浪费时间。编译后的对象可以调用各种正则表达式方法，如findall()、search()等。返回的是一个正则表达式对象。
findall(data)：在字符串data中找到所有与正则表达式pattern_data匹配的子串，并返回一个列表，列表中的每个元素都是一个匹配的字符串。如果没有找到任何匹配，则返回空列表。
所以，re.compile(ptaaern_data).findall(data)的作用就是使用编译好的正则表达式对象，从字符串data中找到所有符合要求的子串，并返回一个匹配的字符串列表。"""
    re_res = re.compile(pattern_data).findall(data)
    return re_res


def res_sub(data, replace, pattern_data=p_data):  # 最后一个参数为默认值
    """
    替换

    :param data:
    :param replace:
    :param pattern_data:
    :return:
    """
    re_res = re.compile(pattern_data).findall(data)
    if re_res:  # 如果存在进行替换,不存在就算了
        return re.sub(pattern_data, replace, data)
    else:
        return re_res


# def params_find(headers,cookies):
def params_find(headers):
    """
    验证请求中是否有${}$信息需要结果关联
    :param headers:
    :param cookies:
    :return:
    """
    if "${" in headers:
        headers = res_find(headers)
    # if  "${" in cookies: #为了保障程序运行去除cookies
    #     cookies=res_find(cookies)
    return headers  # ,cookies   为了保障程序运行去除cookies


def assert_db(db_name, result, db_verify):
    assert_util = AssertUtil()
    # 1初始化
    # sql = init_db("db_1")
    sql = init_db(db_name)
    # 2查询sql
    db_res = sql.fetchone(db_verify)
    log.debug("数据库查询结果:{}".format(str(db_res)))
    # 3 数据库结果与接口返回进行验证
    # 获取数据库结果的key
    verify_list = list(dict(db_res).keys())
    # 根据key获取数据库结果,接口结果
    for line in verify_list:
        res_line = result[line]  # 接口返回的信息
        res_db_line = dict(db_res)[line]  # 数据库返回的信息
        assert_util.assert_body(res_line, res_db_line)

def allure_report(report_path,report_html):
    """
    生成allure报告
    :param report_path:
    :param report_html:
    :return:
    """
    # 定义执行命令
    allure_cmd="allure generate %s -o %s --clean"%(report_path,report_html)
    log.info("报告地址")
    try:
        subprocess.call(allure_cmd,shell=True)
    except:
        log.error("执行用例失败,请检查")
        raise

if __name__ == '__main__':
    #    init_db("db_2")
    print("查询", res_find(data='{"Authorization": "JWT ${token}$"}'))
    print("替换", res_sub(data='{"Authorization": "JWT ${token}$"}', replace="1234"))
