# _*_ coding: utf-8 _*_

import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTouchActionDemo:

    def setup(self):
        JSON_Representation = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".common.MainActivity",
            "noReset": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", JSON_Representation)
        self.driver.implicitly_wait(2)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_stock_price(self):
        ele_find1 = self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/tv_search")
        ele_find1.click()
        ele_find2 = self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/search_input_text")
        ele_find2.click()
        ele_find2.send_keys("alibaba")
        # ele3 = self.driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/name"][@text="阿里巴巴"]')

        locator = (AppiumBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/name"][@text="阿里巴巴"]')
        ele_3 = WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(locator))
        print(ele_3, type(ele_3))

        ele_3.click()
        ele4_price = self.driver.find_element(AppiumBy.XPATH, '//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        assert float(ele4_price) < 200
        # time.sleep(5)
