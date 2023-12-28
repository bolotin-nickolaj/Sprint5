from selenium.webdriver.common.by import By


class Locators:
    #Кнопка "Войти в аккаунт" на главной странице
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    #Ссылка "Регистрация" на странице входа
    REG_REF = (By.XPATH, "//a[@href='/register']")
    #Поля ввода на странице регистрации: имя, почта, пароль
    REG_FIELD1 = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']/fieldset[1]/div/div/input")
    REG_FIELD2 = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']/fieldset[2]/div/div/input")
    REG_FIELD3 = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']/fieldset[3]/div/div/input")
    #Ссылка "Войти" на странице регистрации
    INPUT_IN_REG = (By.XPATH, "//a[@class='Auth_link__1fOlj']")
    #Надпись "Некорректный пароль"
    WRONG_PASSWORD = (By.XPATH, "//p[@class='input__error text_type_main-default']")
    #Кнопка "Зарегистрироваться"
    REG_BUTTON = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']/button")
    #Форма на странице входа и кнопка "Вход"
    INPUT_BUTTON = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']/button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    #Поля ввода на странице Вход: почта, пароль
    INPUT_FIELD1 = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']/fieldset[1]/div/div/input")
    INPUT_FIELD2 = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']/fieldset[2]/div/div/input")
    #Кнопка "Оформить заказ" на главной странице
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    #Ссылка "Восстановить пароль"
    RECOVER_PASSWORD = (By.XPATH, "//a[@href='/forgot-password']")
    #Ссылка на "Личный кабинет"
    PERSONAL_ACCOUNT = (By.XPATH, "//a[@href='/account']")
    #Ссылка на "Историю заказов"
    ORDERS_HISTORY = (By.XPATH,   "//a[@href='/account/order-history']")
    #Поля ввода на странице Личный кабинет: имя, почта, пароль
    PA_FIELD1 = (By.XPATH, "//ul[@class='Profile_profileList__3vTor']/li[1]/div/div/input")
    PA_FIELD2 = (By.XPATH, "//ul[@class='Profile_profileList__3vTor']/li[2]/div/div/input")
    PA_FIELD3 = (By.XPATH, "//ul[@class='Profile_profileList__3vTor']/li[3]/div/div/input")
    #Ссылка "Войти" на странице регистрации
    INPUT_REF_REG_PAGE = (By.XPATH, "//a[@href='/login']")
    #Кнопка "Восстановить" на странице "Восстановление пароля"
    RECOVERY_PWD_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    #Ссылка "Конструктор" из "Личного кабинета"
    DESIGNER_REF = (By.XPATH, "//a[@href='/']")
    #Ссылка "Лента заказов" из "Личного кабинета"
    ORDER_FEED_REF = (By.XPATH, "//a[@href='/feed']")
    #Текст "Лента заказов" в заготовке страницы "Лента заказов"
    ORDER_FEED_TEXT = (By.XPATH, "//h1[@class='text text_type_main-large mt-10 mb-5']")
    #Логотип StellarBurger на странице "Личный кабинет"
    LOGO_ON_PA = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']")
    #Кнопка "Выход" на странице "Личный кабинет"
    EXIT_ON_PA = (By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")
    #Ссылка "Булки"
    DIV_FLEX1 = (By.XPATH, "//div[@style='display: flex;']/div[1]")
    #Ссылка "Соусы"
    DIV_FLEX2 = (By.XPATH, "//div[@style='display: flex;']/div[2]")
    #Ссылка "Начинки"
    DIV_FLEX3 = (By.XPATH, "//div[@style='display: flex;']/div[3]")






