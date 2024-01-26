from utils.YamlUtil import YamlReader
from config import Conf
from config.Conf import ConfigYaml
from utils.RequesetsUtil import Request
import os
import pytest

# 1 获取测试用例内容
# 获取文件路径
test_file = os.path.join(Conf.get_data_path(), "testlogin.yml")  # join用于拼接

# 使用工具类读取多个文档内容
data_list = YamlReader(test_file).data_all()
# print("data_list内容", data_list)

# 2 参数化执行用例


@pytest.mark.parametrize("login", data_list)
def test_yaml(login):
    url = ConfigYaml().get_conf_url() + login["url"]
    print(url)
    json = login["json"]  # data 是从 YAML 文件中读取的，通过 YamlReader(test_file).data_all() 返回的 data_list 中的每一个字典元素中的 data 字段获取的
    res=Request().post(url,json=json )
    #获取token
    try :
        if res['body']['result']['token']:
            token=res['body']['result']['token']
            print(token)
    except:
        print("登录失败,用例执行不通过")
if __name__ == '__main__':
     pytest.main(["-s", "test_login.py"])
