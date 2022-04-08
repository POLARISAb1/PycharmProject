# coding=utf-8
import time

from selenium import webdriver


def test_add_member():
    # 1.登录
    # 2，进入首页页面
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    time.sleep(2)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    time.sleep(10)
    # 3，点击"添加成员"按钮
    driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
    time.sleep(2)
    # 4.填写成员信息
    driver.find_element_by_id("username").send_keys("小花")
    driver.find_element_by_id("memberAdd_acctid").send_keys("001")
    driver.find_element_by_id("memberAdd_biz_mail").send_keys("xiaohua001")
    driver.find_element_by_id("memberAdd_phone").send_keys("18011112222")
    time.sleep(2)
    # 5.点击"保存"按钮
    # 6.进入通讯录页面
    driver.find_element_by_xpath('//*[@id="js_contacts52"]/div/div[2]/div/div[4]/div/form/div[1]/a[2]').click()
    # 7.验证=>断言
