import allure
from selenium import webdriver


class TestAllure:

    @allure.severity(allure.severity_level.BLOCKER)
    def test_allure_01(self):
        print('\n test-----------01')
        assert False
    @allure.severity(allure.severity_level.CRITICAL)
    def test_allure_02(self):
        print('\n test-----------02')

    @allure.severity(allure.severity_level.NORMAL)
    def test_allure_03(self):
        print('\n test-----------03')

    @allure.severity(allure.severity_level.MINOR)
    def test_allure_04(self):
        print('\n test-----------04')

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_allure_05(self):
        print('\n test-----------05')
