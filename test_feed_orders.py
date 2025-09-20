import pytest
import allure
from page_object_main_page import *


@pytest.mark.usefixtures("driver")
class TestFeedOrders:
    
    @allure.title('Проверка перехода на страницу при клике Лента заказов')
    def test_click_button_feed_orders(self):
             
        #"Переход на главную страницу"
        self.driver.get('https://stellarburgers.nomoreparties.site')
        
        #Объект класса страницы
        feed_orders = MainPage(self.driver)

        #"Ожидание закгрузки кнопки 'Лента заказов'"
        feed_orders.wait_button_feed_order()
        
        #"Клик по кнопке 'Лента заказов' на главной странице"
        feed_orders.click_on_button_order_feed()

        #"Ожидание закгрузки кнопки 'Лента заказов'"
        feed_orders.wait_button_feed_order()

        assert feed_orders.current_url() == "https://stellarburgers.nomoreparties.site/feed"


    @allure.title('Проверка открытия окна Детали ингредиента при клике на ингредиент')
    def test_click_info_ingredient(self):
             
        #"Переход на главную страницу"
        self.driver.get('https://stellarburgers.nomoreparties.site')
        
        #Объект класса страницы
        feed_orders = MainPage(self.driver)

        #"Ожидание закгрузки первого ингредиента"
        feed_orders.wait_first_ingredient()

        #"Клик по кнопке первого ингридиента"
        feed_orders.click_on_button_info_ingredient()

        element = feed_orders.find_element(TEXT_INGREDIENT_DETAILS)
        
        assert element.text == "Детали ингредиента"

    @allure.title('Проверка закрытия окна Детали ингредиента')
    def test_close_info_ingredient(self):
             
        #"Переход на главную страницу"
        self.driver.get('https://stellarburgers.nomoreparties.site')
        
        #Объект класса страницы
        feed_orders = MainPage(self.driver)

        #"Ожидание закгрузки первого ингредиента"
        feed_orders.wait_first_ingredient()

        #"Клик по кнопке первого ингридиента"
        feed_orders.click_on_button_info_ingredient()
        
        #"Ожидание кнопки закрытия"
        feed_orders.wait_button_close_info_ingredient()

        #"Клик по кнопке закрытия"
        feed_orders.click_on_button_close_info_ingredient()

        #"Ожидание закгрузки первого ингредиента"
        feed_orders.wait_first_ingredient()

        assert feed_orders.current_url() == "https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa6d"

        
    @allure.title('Проверка при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_ingredient_counter_increases(self):

        #"Переход на главную страницу"
        self.driver.get('https://stellarburgers.nomoreparties.site')
        
        #Объект класса страницы
        feed_orders = MainPage(self.driver)

        #"Ожидание закгрузки первого ингредиента"
        feed_orders.wait_first_ingredient()
        
        ingredient = feed_orders.first_ingredient()

        counter_before =  "0"

        # drag&drop в конструктор
        constructor_area = feed_orders.constructor_area_place()

        feed_orders.drag_and_drop_mouse(ingredient, constructor_area) 

        counter_after = feed_orders.first_ingredient_counter()

        assert int(counter_after) == int(counter_before) + 2
    
