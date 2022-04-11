from time import sleep

import yaml
from selenium import webdriver


def test_operate_cookie():
    driver = webdriver.Chrome()
    # 访问企业微信登录页面
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    # 等待10秒人工扫码操作
    sleep(5)
    # 登录成功后，再去获取 cookie 信息
    cookie = driver.get_cookies()
    # 将cookie存入一个可持久存储的地方，文件
    # 打开文件的时候添加写入权限
    with open('../data/cookie.yml', 'w+') as file:
        yaml.safe_dump(cookie, file)
    # driver.quit()
