import pytest


# params是参数名
@pytest.fixture(scope='function', name='mm')
def my_fixture():
    print('test_pytest/sub前置')
    yield
    print('test_pytest/sub后置')
