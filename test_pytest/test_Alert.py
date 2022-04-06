# _*_ coding: utf-8 _*_
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from test_pytest.test_base import Base


class TestAlert(Base):

    def test_alert(self):
        """
        - 打开网页https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
        - 操作窗口右侧页面，将元素1拖拽到元素2
        - 这时候会有一个alert弹框，点击弹框中的"确定"
        - 然后再按"点击运行"
        - 关闭网页
        :return:
        """
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        sleep(1)
        self.driver.switch_to_frame("iframeResult")
        drag = self.driver.find_element(By.ID, "draggable")
        drop = self.driver.find_element(By.ID, "droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        # action.perform()
        sleep(2)
        self.driver.switch_to_alert().accept()
        self.driver.switch_to_default_content()
        self.driver.find_element(By.ID, "submitBTN")
        sleep(2)



