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
        # pass

    def test_press(self):
        WLAN_ele = self.driver.find_element(AppiumBy.XPATH, "//*[@text='WLAN']")
        TouchAction(self.driver).press(x=150, y=250).release().perform()
        time.sleep(2)
        TouchAction(self.driver).long_press(x=300, y=250, duration=2000).perform()