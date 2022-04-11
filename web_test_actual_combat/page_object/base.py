# coding=utf-8
import yaml
from selenium import webdriver


class Base:

    def __init__(self, driver=None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

            cookies = yaml.safe_load(open('../data/cookie.yml', mode='r'))
            # 植入cookies——cookie是单个的字典信息
            for c in cookies:
                self.driver.add_cookie(c)

            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#indexs")
        else:
            self.driver = driver
