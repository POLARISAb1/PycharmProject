import pytest


def test_raise():
    with pytest.raises(ZeroDivisionError, match='division by zero'):
        raise ZeroDivisionError('division by zero')


def test_raise1():
    with pytest.raises(ValueError) as exc_info:
        raise ValueError('Value must be 42')
    assert exc_info.type is ValueError
    assert exc_info.value.args[0] == 'Value must be 42'
