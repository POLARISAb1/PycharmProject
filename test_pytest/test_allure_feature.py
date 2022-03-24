# coding=utf-8
import allure


@allure.feature("父1")
class TestFeatureStory1:
    @allure.story('子1')
    def test_case1(self):
        print("case1")
        print("case11111111111")

    @allure.story('子2')
    def test_case2(self):
        print("case2")
        print("case22222222222222")

    @allure.story('子3')
    def test_case3(self):
        print("case3")
        print("case33333333333333333333")


@allure.feature("父2")
class TestFeatureStory2:
    @allure.story('子a')
    def test_case_a(self):
        print("case_a")
        print("AAAAAAAAAAAAAAAAAAA")

    @allure.story('子b')
    @allure.step('第一步')
    def test_case_b1(self):
        print("case_b1")
        print("第一步：B1")

    @allure.step('第二步')
    def test_case_b2(self):
        print("case_b2")
        print("第二步：B2")

    @allure.story('子c')
    def test_case_c(self):
        print("case_c")
        print("CCCCCCCCCCCCCCCCCCCCC")
