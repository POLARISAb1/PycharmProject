# coding=utf-8
import allure


class Test1:
    def test_case1(self):
        allure.attach('11111', 'case1')
        pass

    def test_case2(self):
        allure.attach.file('../pic/偷懒.png', '222222', attachment_type=allure.attachment_type.PNG, extension='.png')
        pass

