# _*_ coding: utf-8 _*_
from time import sleep

from selenium.webdriver.common.by import By

from test_pytest.test_base import Base


class TestFile(Base):

    def test_file(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.XPATH, '//*[@id="sttb"]/img[1]').click()
        sleep(2)
        self.driver.find_element(By.ID, "uploadImg").send_keys("../../pic/偷懒.png")
        sleep(2)