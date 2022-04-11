# coding=utf-8

class ContactPage:

    def __init__(self, driver):
        self.driver = driver

    def get_member_names(self):
        """
        获取通讯录成员
        :return:
        """
        # self.driver.find_element_by_xpath('//*[@id="member_list"]/tr[1]/td[2]')
        element = self.driver.find_element_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
        name_list = [ele.get_attribute("title") for ele in element]
        return name_list

