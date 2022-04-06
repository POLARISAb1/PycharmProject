# _*_ coding: utf-8 _*_
from selenium.webdriver.common.by import By

from test_pytest.test_base import Base


class TestFrame(Base):

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element(By.ID, "draggable").text)
        # 切换到父frame
        self.driver.switch_to_default_content()
        # self.driver.switch_to.parent_frame()
        self.driver.find_element(By.ID, "submitBTN").click()
        self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element(By.ID, "droppable").text)
