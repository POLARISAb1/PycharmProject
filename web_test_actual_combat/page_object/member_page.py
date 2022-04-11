# coding=utf-8
import time
from selenium import webdriver


class MemberPage:
    """
    添加成员页面
    """

    def __init__(self, driver):
        self.driver = driver

    def add_member_info(self):
        """
        添加成员信息，并保存
        :return:
        """
        from web_test_actual_combat.page_object.contact_page import ContactPage
        # 填写成员信息
        self.driver.find_element_by_id("username").send_keys("小花")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("001")
        self.driver.find_element_by_id("memberAdd_biz_mail").send_keys("xiaohua001")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("18011112222")
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="js_contacts64"]/div/div[2]/div/div[4]/div/form/div[1]/a[2]').click()
        time.sleep(1)
        return ContactPage(self.driver)


