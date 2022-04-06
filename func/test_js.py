# coding=utf-8
from time import sleep

import pytest
from selenium.webdriver.common.by import By

from test_pytest.test_base import Base


class TestJS1(Base):

    @pytest.mark.skip
    def test_js1(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, "su").click()
        sleep(2)
        self.driver.execute_script("document.documentElement.scrollTop = 10000")
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="page"]/div/a[10]').click()
        sleep(2)

    @pytest.mark.skip
    def test_js2(self):
        self.driver.get("https://www.taobao.com/")
        sleep(2)
        # querySelector()方法返回文档中匹配指定CSS选择器的一个元素。注意： querySelector()方法仅仅返回匹配指定选择器的第一个元素
        self.driver.execute_script('document.querySelector("#J_SiteNavMytaobao").className="site-nav-menu '
                                   'site-nav-mytaobao site-nav-multi-menu J_MultiMenu site-nav-menu-hover"')
        sleep(2)

    def test_js3(self):
        self.driver.get("https://www.12306.cn/index/")
        sleep(2)
        self.driver.execute_script('document.querySelector("#train_date").value="2022-12-22"')
        sleep(2)
        train_date = self.driver.execute_script('return document.querySelector("#train_date").value')
        print(train_date)
        sleep(2)


