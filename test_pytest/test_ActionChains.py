# coding: utf-8
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH, "/html/body/form/input[3]")
        element_dblclick = self.driver.find_element(By.XPATH, "/html/body/form/input[2]")
        element_right_click = self.driver.find_element(By.XPATH, "/html/body/form/input[4]")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_right_click)
        action.double_click(element_dblclick)
        sleep(3)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_move_to_element(self):
        self.driver.get("https://www.baidu.com/?tn=44004473_13_oem_dg")
        move_to_element = self.driver.find_element(By.XPATH, '//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(move_to_element)
        action.perform()

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element(By.XPATH, '//*[@id="dragger"]')
        drop_element = self.driver.find_element(By.XPATH, '/html/body/div[2]')
        action = ActionChains(self.driver)
        # 方法1
        # action.drag_and_drop(drag_element, drop_element)
        # 方法2
        # action.click_and_hold(drag_element).release(drop_element)
        # 方法3
        action.click_and_hold(drag_element).move_to_element(drop_element).release()
        action.perform()

    def test_key(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        element = self.driver.find_element(By.XPATH, "/html/body/label[1]/input")
        element.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

