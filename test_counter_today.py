import pytest
import allure
from page_object_main_page import *



@pytest.mark.usefixtures("driver")
class TestCounterToday:
    
    @allure.title('при создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_counter_completed_for_today(self):
             
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

        "Переход на страницу  'Лента заказов'"
        counter.click_on_button_order_feed()

        counter.wait_header_order_feed()

        number_today_before = counter.number_today()

        counter.click_on_button_constructor()

        counter.wait_first_ingredient()
        
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
        

        #"метод нажатия закрытия окна созданного заказа"
        counter.click_close_id_order()

        #"метод исчезновения модального окна 
        counter.wait_invis_modal_window()

        #"Переход на страницу 'Лента заказов'"
        counter.click_on_button_order_feed()

        #"метод ожидания заголовка  Лента заказов"
        counter.wait_header_order_feed()
   
        #"значение счетчика заказов за все время после оформления заказа"
        number_today_after = counter.number_today()

        
        assert int(number_today_before) == int(number_today_after) - 1


