# _*_ coding: utf-8 _*_

import time
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
        # pass

    def test_pdw(self):
        ele_my = self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")')
        ele_my.click()
        ele_loginin = self.driver.find_element_by_android_uiautomator('new UiSelector().text("帐号密码登录")')
        ele_loginin.click()
        ele_account = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")')
        self.driver.find_element()
        ele_account.send_keys("18625572652")

        ele_password = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")')
        ele_password.send_keys("Yyl990626")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()


    def test_scroll(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.xueqiu.android:id/title_text").text("热门")').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("二鸟说").instance(0));').click()

        time.sleep(3)

    def test_hamcrest(self):
        # assert_that(10, equal_to(10), '这是一个提示')
        # assert_that(10, close_to(7, 2))
        assert_that("ghgre4thgfds", contains_string('4t'))
