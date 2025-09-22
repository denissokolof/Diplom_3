from selenium.webdriver.common.by import By

# Локаторы stellarburgers 

# Главная страница

BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")  # кнопка "Конструктор"

BUTTON_ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")  # кнопка "Лента заказов"

BURGER_INGREDIENT = (By.XPATH, "//a[.//p[text()= 'Флюоресцентная булка R2-D3']]") # Первый ингредиент в разделе "Соберите бургер"

TEXT_COLLECT_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")  # текст "Соберите бургер"

INGREDIENT_COUNTER = (By.XPATH, ".//p[@class='counter_counter__num__3nue1']")  # каунтер первого ингредиента

CONSTRUCTOR_AREA = (By.XPATH, "//div[@class='constructor-element constructor-element_pos_top']")  # зона для перетаскивания ингредиента в заказ

BUTTON_PLACE_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")  # кнопка "Оформить заказ"


# Окно "Детали ингредиента"

TEXT_INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")  # текст "Детали ингредиента"

BUTTON_CLOSE_INGREDIENT_DETAILS = (By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']") # кнопка закрыть "Детали ингредиента"


# Окно "Идентификатор заказа"

NUMBER_ORDER =  (By.XPATH, ".//*[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")  # номер созданного заказа

BUTTON_CLOSE_ORDER_ID = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")  # кнопка закрыть созданный заказ

BUTTON_CLOSE_MODAL = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]") # Ожидание появления кнопки закрытия модального окна

ORDER_MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr") # Ожидание закрытия модального окна

ORDER_NUMBER = (By.CSS_SELECTOR, "h2.text_type_digits-large")


# Страница "Лента заказов"

ORDER_FROM_ORDER_HISTORY = (By.XPATH, ".//p[@class='text text_type_digits-default']")  #  заказ в списке Лента заказов

TEXT_ORDER_FEED = (By.XPATH, ".//*[text()='Лента заказов']")  # текст "Лента заказов"

TEXT_COUNTER_COMPLETED_FOR_ALL_TIME = (By.XPATH, "//div[descendant::p[text()='Выполнено за все время:']]/p[contains(@class, 'OrderFeed_number__2MbrQ')]")  # число счетчика "Выполнено за все время"

TEXT_COUNTER_COMPLETED_FOR_TODAY = (By.XPATH, ".//div[descendant::p[text()='Выполнено за сегодня:']]/p[contains(@class, 'OrderFeed_number__2MbrQ')]")  # число счетчика "Выполнено за сегодня"


# Вход

EMAIL_INPUT = (By.XPATH, "//input[@name='name']")  # поле Email

PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']") # поле пароль

ENTER_BUTTON = (By.XPATH, ".//button[text()='Войти']") # кнопка "Войти"



# Кнопка оформить заказ
BUTTON_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")

# Заголовок модалки с номером заказа
ORDER_ID_TITLE = (By.CSS_SELECTOR, "h2.Modal_modal_title__3ikMw")

# Контейнер модалки заказа
ORDER_MODAL_CONTAINER = (By.CLASS_NAME, "Modal_modal_container__Wo2I_")


# Кнопка "крестик" закрытия модалки
ORDER_MODAL_CLOSE = (By.CLASS_NAME, "Modal_modal__close__TnseK")
