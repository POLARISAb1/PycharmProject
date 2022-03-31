# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.implicitly_wait(3)

    def test_wait(self):
        self.driver.find_element(By.ID, 'ember33').click()
        self.driver.find_element(By.CSS_SELECTOR, "[title~='原创精华文章,有100元奖金']").click()
        print("hello")
        """
        until(self, method, message='')
        until方法需要传入一个method作为参数，method需要接受一个参数，所以wait_show也需要有一个参数
        """
        # 方法1
        def wait_show(x):
            # 定位一组元素用find_elements，elements都是复数
            return len(self.driver.find_elements(By.CSS_SELECTOR, "[title~='招聘内推']")) >= 1
        WebDriverWait(self.driver, 10).until(wait_show)
        # 方法2
        # WebDriverWait(self.driver, 10)
        # .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[title~='招聘内推']")))
        self.driver.find_element(By.CSS_SELECTOR, "[title~='招聘内推']").click()
        print("WORLD")



