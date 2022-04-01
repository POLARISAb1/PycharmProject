# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestGet:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")

    # def test_get_xpath(self):
    #     self.driver.find_element(By.XPATH, '//input[@id="kw"]').send_keys("霍格沃兹测试学院")
    #     print('测试输入')
    #     self.driver.find_element(By.XPATH, '//input[@id="su"]').click()
    #     print('测试搜索')

    def test_css_selector(self):
        self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("霍格沃兹测试学院")
        print('test print')
        self.driver.find_element(By.CSS_SELECTOR, '#su').click()
        print('test search')
