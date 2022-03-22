# coding=utf-8
import pytest

from func.get_excel import get_excel
from func.operation import add_fun


class TestWithEXCEL:
    @pytest.mark.parametrize('x, y, expected', get_excel())
    def test_add(self, x, y, expected):
        assert add_fun(int(x), int(y) == int(expected))
