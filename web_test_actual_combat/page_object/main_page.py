# coding=utf-8
import time


class MainPage:
    """
    首页
    """

    def __init__(self, driver):
        self.driver = driver

    def click_add_member_button(self):
        """
        点击”添加成员“按钮
        :return:
        """
        from web_test_actual_combat.page_object.member_page import MemberPage
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        time.sleep(1)
        return MemberPage(self.driver)
