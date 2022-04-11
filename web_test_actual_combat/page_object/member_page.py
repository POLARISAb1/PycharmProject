# coding=utf-8
import time
from web_test_actual_combat.page_object.base import Base


class MemberPage(Base):
    """
    添加成员页面
    """
    __username = "username"
    __acctid = "memberAdd_acctid"
    __mail = "memberAdd_biz_mail"
    __phone = "memberAdd_phone"
    __btn_save = 'js_btn_save'

    def add_member_info(self, name, acctid, mail, phone):
        """
        添加成员信息，并保存
        :return:
        """

        from web_test_actual_combat.page_object.contact_page import ContactPage
        # 填写成员信息
        self.driver.find_element_by_id(self.__username).send_keys(name)
        self.driver.find_element_by_id(self.__acctid).send_keys(acctid)
        self.driver.find_element_by_id(self.__mail).send_keys(mail)
        self.driver.find_element_by_id(self.__phone).send_keys(phone)
        time.sleep(1)
        self.driver.find_element_by_class_name(self.__btn_save).click()
        return ContactPage(self.driver)


