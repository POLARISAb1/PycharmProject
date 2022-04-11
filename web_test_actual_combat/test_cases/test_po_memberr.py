# _*_ coding: utf-8 _*_

import yaml
from selenium import webdriver

from web_test_actual_combat.test_cases.test_operate_yml import test_operate_cookie
from web_test_actual_combat.page_object.main_page import MainPage


def test_add_member():
    # 登录
    # 进入首页页面
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    # time.sleep(2)
    test_operate_cookie()
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    # 定义cookies，cookie信息从已经写入的cookie文件中获取
    cookies = yaml.safe_load(open('../data/cookie.yml', mode='r'))
    # 植入cookies——cookie是单个的字典信息
    for c in cookies:
        driver.add_cookie(c)

    # driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    # 验证=>断言
    # 链式调用
    # mainPage = MainPage(driver)
    # name_list = mainPage.click_add_member_button().add_member_info().get_member_names()

    # name_list = MainPage.click_add_member_button(MainPage(driver)).add_member_info().get_member_names()

    # --------------这是一条华丽的分割线---------------------------------
    main_page = MainPage(driver)
    print('1111111111')
    member_page = main_page.click_add_member_button()
    print('222222222222')
    contact_page = member_page.add_member_info()
    name_list = contact_page.get_member_names()

    assert '小花' in name_list
    driver.quit()

