from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators

class TestInput:
    # вход по кнопке «Войти в аккаунт» на главной странице
    def test_login_log_into_account_on_main_page(self, driver):
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
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_REF))
        # Нажатие на кнопку «Личный кабинет» на главной странице
        driver.find_element(*Locators.PERSONAL_ACCOUNT_REF).click()
        # Ожидание появления ссылки "История заказов" на странице "Личный кабинет"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDERS_HISTORY))
        # Получение поля ввода "Логин"
        newEmail = driver.find_element(*Locators.EDIT_EMAIL).get_attribute('value')
        # Проверка, что текущее значения логина пользователя соответствует значению, под которым осуществлялся вход.
        assert newEmail == email

    # вход через кнопку «Личный кабинет» на главной странице
    def test_login_via_personal_account_button(self, driver):
        # Нажатие на кнопку «Личный кабинет» на главной странице
        driver.find_element(*Locators.PERSONAL_ACCOUNT_REF).click()
        # Ожидание появления ссылки "Восстановить пароль" на странице "Вход"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.RECOVER_PASSWORD))
        # Значения логина и пароля пользователя, под которыми будет осуществляться вход.
        email = Constants.TEST_EMAIL
        password = Constants.PASSWORD
        # Заполнение полей "Email" и "Пароль" на странице "Вход"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        # Нажатие на кнопку "Войти" на странице "Вход"
        driver.find_element(*Locators.INPUT_BUTTON).click()
        # Ожидание появления кнопки "Личный кабинет" на главной странице
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_REF))
        # Нажатие на кнопку «Личный кабинет» на главной странице
        driver.find_element(*Locators.PERSONAL_ACCOUNT_REF).click()
        # Ожидание появления ссылки "История заказов" на странице "Личный кабинет"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDERS_HISTORY))
        # Получение поля ввода "Логин"
        newEmail = driver.find_element(*Locators.EDIT_EMAIL).get_attribute('value')
        # Проверка, что текущее значения логина пользователя соответствует значению, под которым осуществлялся вход.
        assert newEmail == email

    # вход через кнопку в форме регистрации
    def test_login_via_button_on_registration_form(self, driver):
        # Нажатие на кнопку «Войти в аккаунт» на главной странице
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        # Ожидание появления ссылки "Зарегистрироваться" на странице "Вход"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_REF))
        # Нажатие ссылки "Зарегистрироваться"
        driver.find_element(*Locators.REG_REF).click()
        # Ожидание появления поля ввода имени на странице регистрации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_NAME))
        # Нажатие на ссылку "Войти" на странице регистрация
        driver.find_element(*Locators.INPUT_REF_REG_PAGE).click()
        # Ожидание появления ссылки "Восстановить пароль"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.RECOVER_PASSWORD))
        # Значения логина и пароля пользователя, под которыми будет осуществляться вход.
        email = Constants.TEST_EMAIL
        password = Constants.PASSWORD
        # Заполнение полей "Email" и "Пароль" на странице "Вход"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        # Нажатие на кнопку "Войти" на странице "Вход"
        driver.find_element(*Locators.INPUT_BUTTON).click()
        # Ожидание появления кнопки "Личный кабинет" на главной странице
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_REF))
        # Нажатие на кнопку «Личный кабинет» на главной странице
        driver.find_element(*Locators.PERSONAL_ACCOUNT_REF).click()
        # Ожидание появления ссылки "История заказов" на странице "Личный кабинет"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDERS_HISTORY))
        # Получение поля ввода "Логин"
        newEmail = driver.find_element(*Locators.EDIT_EMAIL).get_attribute('value')
        # Проверка, что текущее значения логина пользователя соответствует значению, под которым осуществлялся вход.
        assert newEmail == email

    # вход через кнопку в форме восстановления пароля
    def test_login_button_password_recovery(self, driver):
        # Нажатие на кнопку «Личный кабинет» на главной странице
        driver.find_element(*Locators.PERSONAL_ACCOUNT_REF).click()
        # Ожидание появления ссылки "Восстановить пароль" на странице "Вход"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.RECOVER_PASSWORD))
        # Нажатие на ссылку "Восстановить пароль" на странице "Вход"
        driver.find_element(*Locators.RECOVER_PASSWORD).click()
        # Ожидание кнопки "Восстановить" на странице "Восстановление пароля"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.RECOVERY_PWD_BUTTON))
        # Нажатие на ссылку "Войти" на странице "Восстановление пароля"
        driver.find_element(*Locators.INPUT_REF_REG_PAGE).click()
        # Ожидание появления ссылки "Восстановить пароль" на странице "Вход"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.RECOVER_PASSWORD))
        # Значения логина и пароля пользователя, под которыми будет осуществляться вход.
        email = Constants.TEST_EMAIL
        password = Constants.PASSWORD
        # Заполнение полей "Email" и "Пароль" на странице "Вход"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        # Нажатие на кнопку "Войти" на странице "Вход"
        driver.find_element(*Locators.INPUT_BUTTON).click()
        # Ожидание появления кнопки "Личный кабинет" на главной странице
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_REF))
        # Нажатие на кнопку «Личный кабинет» на главной странице
        driver.find_element(*Locators.PERSONAL_ACCOUNT_REF).click()
        # Ожидание появления ссылки "История заказов" на странице "Личный кабинет"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDERS_HISTORY))
        # Получение поля ввода "Логин"
        newEmail = driver.find_element(*Locators.EDIT_EMAIL).get_attribute('value')
        # Проверка, что текущее значения логина пользователя соответствует значению, под которым осуществлялся вход.
        assert newEmail == email



