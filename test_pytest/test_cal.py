# coding=utf-8
import pytest

from func.get_yaml import get_value, get_keys, get_errvalue, get_ekeys

# 处理前后置输出结果
from func.calculator import Calculator


@pytest.fixture(scope="function", autouse=True)
def def_fixture():
    print('开始计算')
    yield
    print('结束计算')


@pytest.fixture(scope="module", autouse=True)
def module_fixture():
    yield
    print('结束测试')


@pytest.mark.usefixtures("def_fixture")
class TestCal:

    # 测试加法运算

    @pytest.mark.parametrize("num1,num2,expected", get_value(), ids=get_keys())
    def test_add(self, num1, num2, expected):
        calc1 = Calculator()
        result = calc1.add(num1, num2)
        assert result == expected

    @pytest.mark.parametrize("numa,numb,conclusion", get_errvalue(), ids=get_ekeys())
    def test_add_error(self, numa, numb, conclusion):
        print(numa, numb, conclusion, type(conclusion), eval(conclusion))
        # 定义一个对象calc
        calc = Calculator()
        # eval：把字符串转化为相应对象
        # with pytest.raises（异常类型）:raises 可以捕获到指定异常，并继续下面断言代码，如果异常类型不对，则断言不会执行
        with pytest.raises(eval(conclusion)) as e:
            add_result = calc.add(numa, numb)
            print(add_result)
            assert e.typename == conclusion

