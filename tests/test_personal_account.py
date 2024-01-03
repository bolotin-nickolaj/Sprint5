from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators

# Тестирование перехода в Личный кабинет и Выход их аккаунта
class TestPersonalAccount:
    # переход в личный кабинет по клику на кнопку «Личный кабинет» на главной странице
    def test_click_through_to_the_personal_account(self, first_10_lines_repeated_in_each_of_the_personal_account_tests):
        # Получение поля ввода "Логин"
        newEmail = first_10_lines_repeated_in_each_of_the_personal_account_tests.find_element(*Locators.EDIT_EMAIL).get_attribute('value')
        # Проверка, мы оказались в личном кабинете. Для чего проверяю, что текущее значения логина пользователя соответствует значению, под которым осуществлялся вход.
        assert newEmail == Constants.TEST_EMAIL

    # переход из личного кабинета по клику на ссылку «Конструктор»
    def test_click_through_to_the_designer(self, first_10_lines_repeated_in_each_of_the_personal_account_tests):
        # Нажатие на ссылку "Конструктор" из личного кабинета
        first_10_lines_repeated_in_each_of_the_personal_account_tests.find_element(*Locators.DESIGNER_REF).click()
        # Ожидание появления кнопки "Оформить заказ"
        WebDriverWait(first_10_lines_repeated_in_each_of_the_personal_account_tests, 3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_BUTTON))
        # Проверка, что мы перешли на главную страницу. Для чего проверяю, что текст кнопки  "Войти в аккаунт"/"Оформить заказ" в данном случае равен - "Оформить заказ"
        assert first_10_lines_repeated_in_each_of_the_personal_account_tests.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).text == "Оформить заказ"

    # переход из личного кабинета по клику на логотип Stellar Burgers
    def test_click_through_to_the_stellarburger_logo(self, first_10_lines_repeated_in_each_of_the_personal_account_tests):
        # Нажатие на логотип Stellar Burgers из личного кабинета
        first_10_lines_repeated_in_each_of_the_personal_account_tests.find_element(*Locators.LOGO_ON_PERSONAL_ACCOUNT).click()
        # Ожидание появления кнопки "Оформить заказ"
        WebDriverWait(first_10_lines_repeated_in_each_of_the_personal_account_tests, 3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_BUTTON))
        # Проверка, что мы перешли на главную страницу. Для чего проверяю, что текст кнопки  "Войти в аккаунт"/"Оформить заказ" в данном случае равен - "Оформить заказ"
        assert first_10_lines_repeated_in_each_of_the_personal_account_tests.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).text == "Оформить заказ"

    # выход из личного кабинета по клику на кнопку «Выйти» в личном кабинете
    def test_exit_using_the_logout_button_in_personal_account(self, first_10_lines_repeated_in_each_of_the_personal_account_tests):
        # Нажатие на кнопку "Выход" из личного кабинета
        first_10_lines_repeated_in_each_of_the_personal_account_tests.find_element(*Locators.EXIT_ON_PERSONAL_ACCOUNT).click()
        # Ожидание появления ссылки "Зарегистрироваться" на странице "Вход"
        WebDriverWait(first_10_lines_repeated_in_each_of_the_personal_account_tests, 3).until(EC.visibility_of_element_located(Locators.REG_REF))
        # Проверка, что мы перешли на страницу "Вход". Для чего проверяю, что текст ссылки Locators.REG_REF равен - 'Зарегистрироваться'
        assert first_10_lines_repeated_in_each_of_the_personal_account_tests.find_element(*Locators.REG_REF).text == 'Зарегистрироваться'



