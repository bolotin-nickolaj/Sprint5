from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators

class TestDesigner:
    def test_designer_goto_breads(self, driver):
        driver.find_element(*Locators.DIV_FLEX2).click()
        driver.find_element(*Locators.DIV_FLEX1).click()
        assert driver.find_element(*Locators.DIV_FLEX1).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_designer_goto_sauces(self, driver):
        driver.find_element(*Locators.DIV_FLEX2).click()
        assert driver.find_element(*Locators.DIV_FLEX2).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_designer_goto_toppings(self, driver):
        driver.find_element(*Locators.DIV_FLEX3).click()
        assert driver.find_element(*Locators.DIV_FLEX3).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
