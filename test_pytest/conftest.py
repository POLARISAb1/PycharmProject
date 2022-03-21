import pytest


# params是参数名
@pytest.fixture(scope='function', name='gg')
def my_fixture():
    print('test_pytest前置')
    yield
    print('test_pytest后置')
