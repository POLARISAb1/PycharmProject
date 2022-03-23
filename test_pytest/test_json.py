# coding=utf-8
import pytest

from func.get_add import fun_add
from func.get_json import get_json


class TestGetJson:
    @pytest.mark.parametrize('x, y, expected', get_json())
    def test_json(self, x, y, expected):
        assert fun_add(int(x), int(y)) == int(expected)
