# coding=utf-8



class MemberPage:
    """
    添加成员页面
    """

    def __init__(self):
        pass

    def add_member_info(self):
        """
        添加成员信息，并保存
        :return:
        """
        from web_test_actual_combat.page_object.contact_page import ContactPage
        return ContactPage()