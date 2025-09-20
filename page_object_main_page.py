import allure
from locators import *
from page_object_base_page import *

# Класс главная страница
class MainPage(BasePage):

    #Клик

    @allure.step("метод нажатия кнопки Конструктор")
    def click_on_button_constructor(self):
        self.click(BUTTON_CONSTRUCTOR)

    @allure.step("метод нажатия кнопки Лента заказов")
    def click_on_button_order_feed(self):
        self.click(BUTTON_ORDER_FEED)
    
    @allure.step("метод нажатия кнопки  информация об ингредиенте")
    def click_on_button_info_ingredient(self):
        self.click(BURGER_INGREDIENT)

    @allure.step("метод нажатия кнопки закрытия информации об ингредиенте")
    def click_on_button_close_info_ingredient(self):
        self.click(BUTTON_CLOSE_INGREDIENT_DETAILS)

    @allure.step("метод нажатия кнопки Оформить заказ")
    def click_on_button_order(self):
        self.click(BUTTON_PLACE_ORDER)

    @allure.step("метод нажатия закрытия окна созданного заказа")
    def click_close_id_order(self):
        self.click(BUTTON_CLOSE_ORDER_ID)

    #Ожидания 

    allure.step("метод ожидания загрузки первого ингридиента")
    def wait_first_ingredient(self):
       self.wait_for_element(BURGER_INGREDIENT)

    allure.step("метод ожидания кнопки закрытия окна Детали игредиента")
    def wait_button_close_info_ingredient(self):
        self.wait_for_element(BUTTON_CLOSE_INGREDIENT_DETAILS)

    allure.step("метод ожидания заголовка Детали игредиента")
    def wait_text_datails_ingredients(self):
        self.wait_for_element(TEXT_INGREDIENT_DETAILS)
    
    allure.step("метод ожидания заголовка Соберите бургер")
    def wait_text_collect_burger(self):
        self.wait_for_element(TEXT_COLLECT_BURGER)

    @allure.step("метод ожидания кнопки Конструктор")
    def wait_constructor(self):
        self.wait_for_element(BUTTON_CONSTRUCTOR)

    @allure.step("метод ожидания кнопки Лента заказов")
    def wait_button_feed_order(self):
       self.wait_for_element(BUTTON_ORDER_FEED)

    @allure.step("метод ожидания номера заказа")
    def wait_number_order(self):
       self.wait_for_element(NUMBER_ORDER)


    @allure.step("метод ожидания заголовка  Лента заказов")
    def wait_header_order_feed(self):
       self.wait_for_element(TEXT_ORDER_FEED)

    @allure.step("метод ожидания кликабельности кнопки Лента заказов")
    def wait_clicable_button_feed_order(self):
       self.wait_clicable_element(BUTTON_ORDER_FEED)

    @allure.step("метод ожидания кликабельности кнопки закрыть")
    def wait_clicable_button_close(self):
       self.wait_clicable_element(BUTTON_CLOSE_MODAL)


    @allure.step("метод исчезновения модального окна")
    def wait_invis_modal_window(self):
       self.wait_invis_element(ORDER_MODAL_OVERLAY)


    @allure.step("метод ожидания нового номера заказа")
    def wait_new_order_number(self, old_number):
        self.wait_text_change(ORDER_NUMBER, old_number)

    @allure.step("получение текущего номера заказа")
    def get_order_number(self):
        return self.find_element(ORDER_NUMBER).text.strip()

    @allure.step("Зона конструктора")
    def constructor_area_place(self):
       element = self.find_element(CONSTRUCTOR_AREA)
       return element
    

    @allure.step("Первый ингредиент")
    def first_ingredient(self):
       element = self.find_element(BURGER_INGREDIENT)
       return element
    
    @allure.step("Число счетчика ингредиента")
    def first_ingredient_counter(self):
       element = self.find_element(INGREDIENT_COUNTER).text
       return element
    
    @allure.step("Номер заказа")
    def number_order(self):
       element = self.find_element(NUMBER_ORDER).text
       return element

    @allure.step("Номер заказа в истории")
    def number_order_history(self):
       element = self.find_element(ORDER_FROM_ORDER_HISTORY).text
       return element
    
    @allure.step("Число счетчика за все время")
    def number_all_time(self):
       element = self.find_element(TEXT_COUNTER_COMPLETED_FOR_ALL_TIME).text
       return element
    
    @allure.step("Число счетчика за сегодня")
    def number_today(self):
       element = self.find_element(TEXT_COUNTER_COMPLETED_FOR_TODAY).text
       return element

    

    #Вход

    @allure.step(" Вход ")
    def login(self, email, password):
    
        #Поле "Email"
        self.click(EMAIL_INPUT)
        self.find_element(EMAIL_INPUT).send_keys(email)

        #Поле "Пароль"
        self.click(PASSWORD_INPUT)
        self.find_element(PASSWORD_INPUT).send_keys(password)

        #Клик по кнопке "Войти"
        self.click(ENTER_BUTTON)
       

    allure.step("метод ожидания кнопки Войти")
    def wait_button_enter(self):
        self.wait_for_element(ENTER_BUTTON)