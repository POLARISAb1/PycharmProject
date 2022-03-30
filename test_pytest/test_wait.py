# coding=utf-8
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")

    def test_wait(self):
        self.driver.find_element(By.ID, 'ember33').click()
        sleep(3)
        self.driver.find_element(By.ID, 'ember35').click()
        print("hello")
