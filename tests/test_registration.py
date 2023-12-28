from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators

faker = Faker()


class TestRegistration:
    def test_registration_wrong_password(self, driver):
        email = faker.email()
        password = 12345
        WebDriverWait(driver,3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_BUTTON))
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_REF))
        driver.find_element(*Locators.REG_REF).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_FIELD1))
        driver.find_element(*Locators.REG_FIELD3).send_keys(password)
        driver.find_element(*Locators.REG_FIELD2).click()
        assert len(driver.find_elements(*Locators.WRONG_PASSWORD)) == 1

    def test_registration_success(self, driver):
        email = faker.email()
        password = Constants.PASSWORD
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_REF))
        driver.find_element(*Locators.REG_REF).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_FIELD1))
        driver.find_element(*Locators.REG_FIELD1).send_keys(Constants.NAME)
        driver.find_element(*Locators.REG_FIELD2).send_keys(email)
        driver.find_element(*Locators.REG_FIELD3).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.RECOVER_PASSWORD))
        driver.find_element(*Locators.INPUT_FIELD1).send_keys(email)
        driver.find_element(*Locators.INPUT_FIELD2).send_keys(password)
        driver.find_element(*Locators.INPUT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT))
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDERS_HISTORY))
        newName = driver.find_element(*Locators.PA_FIELD1).get_attribute('value')
        newEmail = driver.find_element(*Locators.PA_FIELD2).get_attribute('value')

        assert newName == Constants.NAME and newEmail == email
