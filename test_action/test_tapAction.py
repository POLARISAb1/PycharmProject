# _*_ coding: utf-8 _*_
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


class TestTouchActionDemo:

    def setup(self):
        JSON_Representation = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.android.settings",
            "appActivity": ".Settings",
            "noReset": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", JSON_Representation)
        self.driver.implicitly_wait(2)

    def teardown(self):
        self.driver.quit()

    def test_tap_action(self):
        action = TouchAction(self.driver)
        WLAN_ele = self.driver.find_element(AppiumBy.XPATH, "//*[@text='WLAN']")
        action.tap(WLAN_ele).perform()
        time.sleep(3)
