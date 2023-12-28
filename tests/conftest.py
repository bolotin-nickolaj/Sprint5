import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Constants.URL)
    yield driver
    driver.quit()

@pytest.fixture
def pa_driver(driver):
    driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_REF))
    email = Constants.TEST_EMAIL
    password = Constants.PASSWORD
    driver.find_element(*Locators.INPUT_FIELD1).send_keys(email)
    driver.find_element(*Locators.INPUT_FIELD2).send_keys(password)
    driver.find_element(*Locators.INPUT_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_BUTTON))
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDERS_HISTORY))
    return driver

