import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators
from urls import Urls


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.URL)
    yield driver
    driver.quit()

# Фикстура содержит 10 первых строк, повторяющихся в каждом из тестов Личного кабинета
# В результате шагов фикстуры пользователь авторизуется и оказывается в личном кабинете
@pytest.fixture
def first_10_lines_repeated_in_each_of_the_personal_account_tests(driver):
    # Нажатие на кнопку «Войти в аккаунт» на главной странице
    driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
    # Ожидание появления ссылки "Зарегистрироваться" на странице "Вход"
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_REF))
    # Значения логина и пароля пользователя, под которыми будет осуществляться вход.
    email = Constants.TEST_EMAIL
    password = Constants.PASSWORD
    # Заполнение полей "Email" и "Пароль" на странице "Вход"
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
    # Нажатие на кнопку "Войти" на странице "Вход"
    driver.find_element(*Locators.INPUT_BUTTON).click()
    # Ожидание появления кнопки "Личный кабинет" на главной странице
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_BUTTON))
    # Нажатие на кнопку «Личный кабинет» на главной странице
    driver.find_element(*Locators.PERSONAL_ACCOUNT_REF).click()
    # Ожидание появления ссылки "История заказов" на странице "Личный кабинет"
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDERS_HISTORY))
    return driver

