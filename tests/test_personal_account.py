from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators

class TestPersonalAccount:
    def test_pa_go_from_personal_account(self, pa_driver):
        newName = pa_driver.find_element(*Locators.PA_FIELD1).get_attribute('value')
        newEmail = pa_driver.find_element(*Locators.PA_FIELD2).get_attribute('value')
        assert newName == Constants.NAME and newEmail == Constants.TEST_EMAIL

    def test_pa_go_to_designer_from_pers_account(self, pa_driver):
        pa_driver.find_element(*Locators.DESIGNER_REF).click()
        WebDriverWait(pa_driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_BUTTON))
        assert pa_driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).text == "Оформить заказ"

    def test_pa_go_to_logo_stellarburger_from_pers_account(self, pa_driver):
        pa_driver.find_element(*Locators.LOGO_ON_PA).click()
        WebDriverWait(pa_driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_BUTTON))
        assert pa_driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).text == "Оформить заказ"

    def test_pa_exit(self, pa_driver):
        pa_driver.find_element(*Locators.EXIT_ON_PA).click()
        WebDriverWait(pa_driver, 3).until(EC.visibility_of_element_located(Locators.REG_REF))
        assert pa_driver.find_element(*Locators.REG_REF).text == 'Зарегистрироваться'



