from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators

class TestInput:
    def test_login_log_into_account_on_main_page(self, driver):
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_REF))
        email = Constants.TEST_EMAIL
        password = Constants.PASSWORD
        driver.find_element(*Locators.INPUT_FIELD1).send_keys(email)
        driver.find_element(*Locators.INPUT_FIELD2).send_keys(password)
        driver.find_element(*Locators.INPUT_BUTTON).click()
        WebDriverWait(driver,3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_BUTTON))
        assert driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).text == "Оформить заказ"

    def test_login_via_personal_account_button(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.RECOVER_PASSWORD))
        email = Constants.TEST_EMAIL
        password = Constants.PASSWORD
        driver.find_element(*Locators.INPUT_FIELD1).send_keys(email)
        driver.find_element(*Locators.INPUT_FIELD2).send_keys(password)
        driver.find_element(*Locators.INPUT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_BUTTON))
        assert driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).text == "Оформить заказ"

    def test_login_via_button_on_registration_form(self, driver):
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_REF))
        driver.find_element(*Locators.REG_REF).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_FIELD1))
        driver.find_element(*Locators.INPUT_REF_REG_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.RECOVER_PASSWORD))
        email = Constants.TEST_EMAIL
        password = Constants.PASSWORD
        driver.find_element(*Locators.INPUT_FIELD1).send_keys(email)
        driver.find_element(*Locators.INPUT_FIELD2).send_keys(password)
        driver.find_element(*Locators.INPUT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_BUTTON))
        assert driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).text == "Оформить заказ"

    def test_login_button_password_recovery(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.RECOVER_PASSWORD))
        driver.find_element(*Locators.RECOVER_PASSWORD).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.RECOVERY_PWD_BUTTON))
        driver.find_element(*Locators.INPUT_REF_REG_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.RECOVER_PASSWORD))
        email = Constants.TEST_EMAIL
        password = Constants.PASSWORD
        driver.find_element(*Locators.INPUT_FIELD1).send_keys(email)
        driver.find_element(*Locators.INPUT_FIELD2).send_keys(password)
        driver.find_element(*Locators.INPUT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_BUTTON))
        assert driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).text == "Оформить заказ"



