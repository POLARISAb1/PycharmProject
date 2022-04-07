# coding=utf-8
from func.main import Main


class TestPageObject:

    def setup(self):
        main = Main()
        main.click_first_link().title()
        