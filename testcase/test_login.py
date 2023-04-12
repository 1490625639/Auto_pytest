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
print("data_list内容", data_list)

# 2 参数化执行用例
"""数据参数化就是将测试数据从测试代码中分离出来，
    将测试数据单独存放在一个数据源中（比如：Excel、CSV、YAML、JSON等），
     然后通过测试框架读取这些数据，动态地生成多组测试用例，
      从而减少重复编写代码的工作量，提高测试的效率
举个例子，比如我们要测试一个加法函数，我们可以把不同的加数和被加数放在一个数据源中，然后使用数据参数化技术自动生成多组测试数据来测试我们的加法函数"""


@pytest.mark.parametrize("login", data_list)  # 先参数化,这里不懂复习mark这个函数
def test_yaml(login):
    # 初始化url,data等数据  这里进行初始化
    url = ConfigYaml().get_conf_url() + login["url"]  # url拼接 http+具体接口信息
    print(url)
    data = login["data"]  # data 是从 YAML 文件中读取的，通过 YamlReader(test_file).data_all() 返回的 data_list 中的每一个字典元素中的 data 字段获取的
    """data_list能被login["data"]识别出来的原因:
在测试方法中，@pytest.mark.parametrize 装饰器将 data_list 列表中的数据逐一传递给 
test_yaml 函数，并将其中的每个字典都作为 login 参数传入。
因此，在 test_yaml 函数中，login 参数的值实际上就是 data_list 列表中的一个字典，
其中包含了 url 和 data 两个键值对。可以通过 login["url"] 和 login["data"] 来获取相应的值。"""
    print("data数据:", data)
    # post请求
    request = Request()
    res = request.post(url, data=data)
    # 结果
    print("返回结果", res)

if __name__ == '__main__':
    pytest.main(["-s", "--nohtml", "test_login.py"])
# 4.13 00点34分不在家，不写代码