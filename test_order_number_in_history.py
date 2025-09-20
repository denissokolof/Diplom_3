import pytest
import allure
from page_object_main_page import *



@pytest.mark.usefixtures("driver")
class TestOrderNumber:
    
    @allure.title('Заказ в ленте история заказов')
    def test_counter_completed_for_all_time(self):
             
        #"Переход на страницу входа"
        self.driver.get('https://stellarburgers.nomoreparties.site/login')
        
        #Объект класса страницы
        counter = MainPage(self.driver)

        #"Ожидание закгрузки заголовка 'Вход'"
        counter.wait_button_enter()

        #"Вход"
        counter.login("denissokolov1998@yandex.ru", "denis1998")

        #"Ожидание закгрузки заголовка 'Соберите бургер'"
        counter.wait_text_collect_burger()
        
        #Добавление ингредиента в заказ
        ingredient = counter.first_ingredient()
        constructor_area = counter.constructor_area_place()
        counter.drag_and_drop_mouse(ingredient, constructor_area)
        
        #Кнопка заказать 
        counter.click_on_button_order()

        # Получаем старый номер
        old_number = counter.get_order_number()

        # Ждём, пока появится новый
        counter.wait_new_order_number(old_number)
        

        number_id = counter.number_order()
        
        #"метод нажатия закрытия окна созданного заказа"
        counter.click_close_id_order()

        #"метод исчезновения модального окна 
        counter.wait_invis_modal_window()

        #"Переход на страницу 'Лента заказов'"
        counter.click_on_button_order_feed()

        #"метод ожидания заголовка  Лента заказов"
        counter.wait_header_order_feed()

        number_id_hustory = counter.number_order_history()
        
        assert number_id in number_id_hustory


