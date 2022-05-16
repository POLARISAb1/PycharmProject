from typing import List

import pytest


# params是参数名
@pytest.fixture(scope='function', name='mm')
def my_fixture():
    print('test_pytest/sub前置')
    yield
    print('test_pytest/sub后置')

def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")
