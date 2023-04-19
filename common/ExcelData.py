from utils.ExcelUtil import ExcelReader
from common.ExcelConfig import DataConfig


class Data:
    def __init__(self, testcase_file, sheet_name):
        # 1 获取要运行的列表
        # self.reader = ExcelReader("../data/testdata.xlsx", "美多商城接口测试")
        self.reader = ExcelReader(testcase_file, sheet_name)
        # print(reader.data())

    def get_run_data(self):
        # 2 读取列是否运行 y
        run_list = list()  # 类似ExcelUtil文件，定义一个空列表 []=list()
        for line in self.reader.data():
            if str(line[DataConfig().is_run]) == "y":  # 这里判断是否运行列名不符合 规范,excel列的映射,ExcelConfig
                print(line)
                # 3 运行后的放入新的列表
                run_list.append(line)
        return run_list
        print(run_list)
    def get_case_list(self):
        """获取全部测试用例"""
  # 2 读取列是否运行 y
        run_list=list()
        # for line in self.reader.data():
        #         run_list.append(line)
        #使用列表推导式
        run_list=[line for line in self.reader.data()]
        return run_list
    def get_case_pre(self,pre):# 根据前置条件,从全部测试用例中取对应的测试用例
        run_list=self.get_case_list()
        for line in run_list:
            if pre in   dict(line).values():
                return pre
            return None