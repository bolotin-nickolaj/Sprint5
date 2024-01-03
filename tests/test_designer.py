from locators import Locators

# Тестирование раздела "Конструктор". Нужно проверить, что работают переходы к разделам: "Булки", "Соусы", "Начинки"
class TestDesigner:
    # Нужно проверить, что работает переход к разделу "Булки"
    def test_transition_to_breads_section_is_working(self, driver):
        # Нажатие на раздел "Соусы"
        driver.find_element(*Locators.DIV_SAUCES).click()
        # Нажатие на раздел "Булки"
        driver.find_element(*Locators.DIV_BREADS).click()
        # Проверка, что раздел "Булки" теперь активен. Для чего проверим наличие в наименовании CLASS'а данного раздела текста, указывающего, что данный раздел текущий.
        assert 'tab_tab_type_current__2BEPc' in driver.find_element(*Locators.DIV_BREADS).get_attribute('class')

    # Нужно проверить, что работает переход к разделу "Соусы"
    def test_transition_to_sauces_section_is_working(self, driver):
        # Нажатие на раздел "Соусы"
        driver.find_element(*Locators.DIV_SAUCES).click()
        # Проверка, что раздел "Соусы" теперь активен. Для чего проверим наличие в наименовании CLASS'а данного раздела текста, указывающего, что данный раздел текущий.
        assert 'tab_tab_type_current__2BEPc' in driver.find_element(*Locators.DIV_SAUCES).get_attribute('class')

    # Нужно проверить, что работает переход к разделу "Начинки"
    def test_transition_to_toppings_section_is_working(self, driver):
        # Нажатие на раздел "Начинки"
        driver.find_element(*Locators.DIV_TOPPINGS).click()
        # Проверка, что раздел "Начинки" теперь активен. Для чего проверим наличие в наименовании CLASS'а данного раздела текста, указывающего, что данный раздел текущий.
        assert 'tab_tab_type_current__2BEPc' in driver.find_element(*Locators.DIV_TOPPINGS).get_attribute('class')
