import pytest


# params是参数名
@pytest.fixture(scope='function', params=['猪猪', '牛牛', '兔兔'], name='all_in')
def my_fixture(request):
    # 固定写法

    # print('前置')
    # yield
    # # yield和return不可以一起用
    # print('后置')
    # # request.param属性名
    # return request.param

    print('all前置')
    yield request.param
    print('all后置')
