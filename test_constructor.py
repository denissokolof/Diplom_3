import pytest
import allure
from page_object_main_page import *

@pytest.mark.usefixtures("driver")
class TestConstructor:
    
    @allure.title('Проверка перехода на главную страницу при клике Конструктор')
    def test_click_button_constructor(self):
             
        #"Переход на страницу лента заказов"
        self.driver.get('https://stellarburgers.nomoreparties.site/feed')
        
        #Объект класса страницы
        constructor = MainPage(self.driver)

        #"Ожидание закгрузки кнопки Конструктор"
        constructor.wait_constructor()
        
        #"Клик по кнопке 'Конструктор' на главной странице"
        constructor.click_on_button_constructor()

        #"Ожидание закгрузки кнопки Конструктор"
        constructor.wait_constructor()

        assert constructor.current_url() == "https://stellarburgers.nomoreparties.site/"
        



    
    
