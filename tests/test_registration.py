from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from constants import Constants
from locators import Locators

faker = Faker()


# Проверка функционала Регистрация
class TestRegistration:
    # Проверить, что выдается ошибка в случае ввода некорректного пароля, в частности длина пароля < 6 символов
    def test_registration_wrong_password(self, driver):
        email = faker.email()
        password = 12345
        WebDriverWait(driver,3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_BUTTON))
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_REF))
        driver.find_element(*Locators.REG_REF).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_NAME))
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_EMAIL).click()
        assert driver.find_element(*Locators.WRONG_PASSWORD).text == 'Некорректный пароль'

    # Проверить успешную регистрацию. Для чего после регистрации перейдем в личный кабинет и сравним значения Имени и Емейла пользователя с введенными при регистрации
    def test_registration_success(self, driver):
        email = faker.email()
        password = Constants.PASSWORD
        # Нажатие на кнопку "Войти в аккаунт" на главной странице
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_REF))
        # Нажать на ссылку "Зарегистрированться" на странице "Вход"
        driver.find_element(*Locators.REG_REF).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_NAME))
        # Заполнить поля ввода: имя, емейл, пароль на странице "Регистрация"
        driver.find_element(*Locators.REG_NAME).send_keys(Constants.NAME)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        # Нажать на кнопку "Зарегистрироваться"
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.RECOVER_PASSWORD))
        # Заполнить поля ввода емейла и пароля на странице "Вход"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        # Нажать на кнопку "Войти" на странице "Вход"
        driver.find_element(*Locators.INPUT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_REF))
        # Нажать на ссылку "Личный кабинет" на главной странице
        driver.find_element(*Locators.PERSONAL_ACCOUNT_REF).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDERS_HISTORY))
        # Получение Имени и Емейла пользователя из личного кабинета
        newName = driver.find_element(*Locators.EDIT_NAME).get_attribute('value')
        newEmail = driver.find_element(*Locators.EDIT_EMAIL).get_attribute('value')
        # Проверить, что значения Имени и Емейла пользователя совпадают с введенными при регистрации
        assert newName == Constants.NAME and newEmail == email
