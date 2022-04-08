# coding=utf-8



class MainPage:
    """
    首页
    """

    def __init__(self):
        pass

    def click_add_member_button(self):
        """
        点击”添加成员“按钮
        :return:
        """
        from web_test_actual_combat.page_object.member_page import MemberPage
        return MemberPage()
