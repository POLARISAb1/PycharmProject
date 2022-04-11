# coding=utf-8
from web_test_actual_combat.page_object.base import Base


class ContactPage(Base):
    __member = ".member_colRight_memberTable_td:nth-child(2)"

    def get_member_names(self):
        """
        获取通讯录成员
        :return:
        """

        element = self.driver.find_elements_by_css_selector(self.__member)
        name_list = [ele.get_attribute("title") for ele in element]
        return name_list
