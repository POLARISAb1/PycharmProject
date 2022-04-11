# coding=utf-8
import time

from web_test_actual_combat.page_object.base import Base


class MainPage(Base):
    """
    首页
    """
    __link_text = '添加成员'

    def click_add_member_button(self):
        """
        点击”添加成员“按钮
        :return:
        """

        from web_test_actual_combat.page_object.member_page import MemberPage
        self.driver.find_element_by_link_text(self.__link_text).click()

        time.sleep(1)
        return MemberPage(self.driver)
