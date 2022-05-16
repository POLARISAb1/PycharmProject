# _*_ coding: utf-8 _*_

import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *


class TestTouchActionDemo:

    def setup(self):
        JSON_Representation = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".common.MainActivity",
            "noReset": "true",
            "skipServerInstallation": "true",
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", JSON_Representation)
        self.driver.implicitly_wait(2)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('search_key, content, expect_price', [["alibaba", '阿里巴巴', 80], ["jingd", "京东",  55]])
    def test_cs(self, search_key, content, expect_price):
        # 首先判断阿里巴巴的价格
        self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/tv_search").click()
        # self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/search_input_text").click()
        self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(search_key)
        locator = (AppiumBy.XPATH, f'//*[@resource-id="com.xueqiu.android:id/name"][@text="{content}"]')
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(locator)).click()
        price_element = self.driver.find_element(AppiumBy.XPATH, f'//*[@text="{content}" and @resource-id="com.xueqiu.android:id/stockName"]'
                                                                 '/../..//android.widget.LinearLayout[2]/*[@resource-id="com.xueqiu.android:id'
                                                                 '/current_price"]').text
        current_price = float(price_element)
        print(current_price)
        assert_that(current_price, close_to(expect_price, expect_price*0.1))





