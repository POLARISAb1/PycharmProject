# coding=utf-8
import allure


class TestSearch:
    @allure.title("搜索词为android")
    def test_case1(self):
        print("case1")

    @allure.title("搜索词为ios")
    def test_case2(self):
        print("case2")
