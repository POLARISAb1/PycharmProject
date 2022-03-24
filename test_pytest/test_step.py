# coding=utf-8
import allure
import pytest


@pytest.mark.parametrize('user, key', [[1, 'something'], [2, None], [3, 'anything']])
@allure.step('@allure.step:进行登录， 用户名: {user}, 密码: {key}')
def test_steps(user, key):
    with allure.step('with allure.step:进行登录， 用户名: {user}, 密码: {key}'):
        print('Step测试用例')
