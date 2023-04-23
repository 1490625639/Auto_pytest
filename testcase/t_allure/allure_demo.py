import pytest
import allure


@allure.feature("接口测试,这是一个一级标签")  # 标签
class TestAllure:
    # 测试方法
    @allure.severity(allure.severity_level.BLOCKER)  # 级别
    @allure.story("这是一个二级标签,test1")  # 二级标签
    @allure.title("测试标题1")  # 标题
    @allure.description("执行的测试用例1 的描述")  # 描述
    def test_1(self):
        print("测试方法1")

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("这是一个二级标签,test1")
    @allure.title("测试标题2")
    @allure.description("执行的测试用例1 的描述")
    def test_2(self):
        print("测试方法2")

    @allure.story("这是一个二级标签,test3")
    @allure.title("测试标题3")
    @allure.description("执行的测试用例1 的描述")
    def test_3(self):
        print("测试方法3")
    @pytest.mark.parametrize("case",["case1","case2"])
    def test_4(self,case):
        print(case)
        allure.dynamic.title(case)

if __name__ == '__main__':
    pytest.main(["allure_demo"])
