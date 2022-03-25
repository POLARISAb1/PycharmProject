# coding=utf-8
import pytest


# 处理前后置输出结果
# class FixtureDemo:
#     @pytest.fixture(scope="function", params="", autouse=True)
#     def def_fixture(self):
#         print('开始计算')
#         yield
#         print('结束计算')
#
#     @pytest.fixture()
#     def module_fixture(self):
#         yield
#         print('结束测试')


# 编写测试用例
class TestCal:

    # 测试加法运算
    @pytest.mark.parametrize("num1,num2,expected", [[1, 1, 2], [2, 3, 4]])
    def test_add(self, num1, num2, expected):
        assert num1 + num2 == expected

    # 测试乘法运算
    # def test_div(self):
    #     pass
