import pytest
import allure
from Diplom_3.pages.page_object_main_page import MainPage


class TestConstructor:
    
    @allure.title('Проверка перехода на главную страницу при клике Конструктор')
    def test_click_button_constructor(self, driver):
             
        #"Переход на страницу лента заказов"
        driver.get('https://stellarburgers.nomoreparties.site/feed')
        
        #Объект класса страницы
        constructor = MainPage(driver)

        #"Ожидание закгрузки кнопки Конструктор"
        constructor.wait_constructor()
        
        #"Клик по кнопке 'Конструктор' на главной странице"
        constructor.click_on_button_constructor()

        #"Ожидание закгрузки кнопки Конструктор"
        constructor.wait_constructor()

        assert constructor.current_url() == "https://stellarburgers.nomoreparties.site/"
        



    
    
