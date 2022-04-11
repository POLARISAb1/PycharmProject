# _*_ coding: utf-8 _*_
import allure
from faker import Faker
from web_test_actual_combat.page_object.main_page import MainPage


@allure.title('测试企业微信主页的添加成员')
def test_add_member():

    fake = Faker(locale='zh_CN')
    name = fake.name()
    acctid = fake.ssn()
    mail = fake.pystr(min_chars=0, max_chars=8)
    phone = fake.phone_number()
    # main_page = MainPage()
    # member_page = main_page.click_add_member_button()
    # contact_page = member_page.add_member_info(name=name, acctid=acctid, mail=mail, phone=phone)
    # name_list = contact_page.get_member_names()
    # 链式调用
    name_list = MainPage().click_add_member_button()\
        .add_member_info(name=name, acctid=acctid, mail=mail, phone=phone)\
        .get_member_names()
    print(name_list)
    # 验证=>断言
    assert name in name_list


