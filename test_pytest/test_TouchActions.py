# _*_ coding: utf-8 _*_
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction:

    def setup(self):
        # 在创建 driver 对象时，添加浏览器的 option 选项 关闭 w3c 模式
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touch_actions(self):
        self.driver.get("http://www.baidu.com")
        input_element = self.driver.find_element_by_id("kw")
        input_element.send_keys("selenium测试")
        search_element = self.driver.find_element_by_id("su")
        action = TouchActions(self.driver)
        action.tap(search_element)

        action.scroll_from_element(search_element, 0, 10000)
        action.perform()
        sleep(3)



