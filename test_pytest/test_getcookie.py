# coding=utf-8
from time import sleep

import yaml

from test_pytest.test_base import Base


class TestGetCookie(Base):

    def test_get_cookie(self):
        # 访问企业微信登录页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 等待10秒人工扫码操作
        sleep(10)
        # 登录成功后，再去获取 cookie 信息
        cookie = self.driver.get_cookies()
        # 将cookie存入一个可持久存储的地方，文件
        # 打开文件的时候添加写入权限
        with open('../data/cookie.yml', 'w+') as file:
            yaml.safe_dump(cookie, file)

    def test_add_cookie(self):
        # 访问企业微信主界面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # 定义cookies，cookie信息从已经写入的cookie文件中获取
        cookies = yaml.safe_load(open('../data/cookie.yml', mode='r'))
        sleep(5)
        # 植入cookies——cookie是单个的字典信息
        for c in cookies:
            self.driver.add_cookie(c)
        sleep(5)
        # 再次访问企业微信页面，发现无需扫码自动登录，而且可以多次使用
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        sleep(5)
