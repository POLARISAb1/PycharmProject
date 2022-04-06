# _*_ coding: utf-8 _*_
from time import sleep

from test_pytest.test_base import Base


class TestWindow(Base):

    def test_Window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.window_handles)
        # 所有的窗口输出是个列表
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("123")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("13800000000")
        self.driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("123")
        sleep(3)
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("13800000000")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("123")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)

