# _*_ coding: utf-8 _*_
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

JSON_Representation = {
    "platformName": "android",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings",
    "noReset": "true"
}


def test__xueqiu():
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", JSON_Representation)
    driver.implicitly_wait(5)
    # - 打开【雪球】应用首页
    # - 定位首页的搜索框
    # el1 = driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/tv_search")
    # # - 判断搜索框的是否可用，并查看搜索框name属性值
    # print(el1.is_enabled())
    # print(el1.text)
    # # - 打印搜索框这个元素的左上角坐标和它的宽高
    # print(el1.location)
    # print(el1.size)
    # # - 向搜索框输入：alibaba
    # el1.click()
    # el2 = driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/search_input_text")
    # el2.click()
    # el2.send_keys("alibaba")
    # # - 判断【阿里巴巴】是否可见
    # el3 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("阿里巴巴")')
    # el3en = el3.get_attribute("displayed")
    # # - 如果可见，打印“搜索成功”点击，如果不可见，打印“搜索失败”
    # if el3en == "true":
    #     print("搜索成功")
    # else:
    #     print("搜索失败")

    # action = TouchAction(driver)
    # action.press(x=361, y=484).wait(200).move_to(x=361, y=427).release().perform()
    # action.swipe()
    # can_scroll_more = driver.execute_script('mobile: scrollGesture', {
    #     'left': 23, 'top': 100, 'width': 600, 'height': 1500,
    #     'direction': 'down',
    #     'percent': 2.0
    # })
    # print(driver.get_window_rect())

    # driver.swipe(476, 1086, 476, 387)
    # time.sleep(5)

    # ele_li = driver.find_elements(By.ID, "com.android.settings:id/title")
    # for ele in ele_li:
    #     print(ele.get_attribute("enabled"))
    #     print(ele.get_attribute("resource-id"))
    #     print(ele.get_attribute("name"))
    app_ele = driver.find_element(AppiumBy.XPATH, "//*[@text='应用']")
    more_ele = driver.find_element(AppiumBy.XPATH, "//*[@text='更多']")
    driver.drag_and_drop(app_ele, more_ele)
    driver.quit()
