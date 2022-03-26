# coding=utf-8
import pytest


# 处理前后置输出结果
@pytest.fixture(scope="function", autouse=True)
def def_fixture():
    print('开始计算')
    yield
    print('结束计算')


@pytest.fixture(scope="module", autouse=True)
def module_fixture():
    yield
    print('结束测试')


# 编写测试用例
from func.get_yaml import get_yaml


@pytest.mark.usefixtures("def_fixture")
class TestCal:

    # 测试加法运算

    @pytest.mark.parametrize("num1,num2,expected", get_yaml())
    def test_add(self, num1, num2, expected):
        assert num1 + num2 == expected

    # 测试乘法运算
    # def test_div(self):
    #     pass
