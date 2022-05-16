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
            "appActivity": ".ChooseLockPattern",
            "noReset": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", JSON_Representation)
        self.driver.implicitly_wait(2)

    def teardown(self):
        # self.driver.quit()
        pass


    def test_move_to(self):
        TouchAction(self.driver).press(x=200, y=485).move_to(x=357, y=485).move_to(x=360, y=643).move_to(x=360, y=800).release().perform()
        time.sleep(2)
