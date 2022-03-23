# coding=utf-8
import pytest

from func.get_add import fun_add
from func.get_csv import get_csv


class TestGetCsv:
    @pytest.mark.parametrize('x, y, expected', get_csv())
    def test_add(self, x, y, expected):
        assert fun_add(int(x), int(y)) == int(expected)
