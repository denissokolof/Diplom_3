import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Класс главная страница
class BasePage:

    def __init__(self, driver):
        self.driver = driver
    
    allure.step("метод поиска элемента")
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step("метод нажатия кнопки")
    def click(self, locator):
        return self.driver.find_element(*locator).click()
    
    allure.step("метод ожидания видимости элемента")
    def wait_for_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_any_elements_located(locator))
    
    allure.step("метод ожидания кликабельности элемента")
    def wait_clicable_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    
    allure.step("метод ожидания исчезновения элемента")
    def wait_invis_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
    
    allure.step("метод ожидания видимости элемента")
    def wait_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    allure.step("метод получения URL")
    def current_url(self):
        return self.driver.current_url
    
    allure.step("метод ожидания видимости элемента и изменение параметра")
    def wait_text_change(self, locator, old_text, timeout=30):
        WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element(*locator).text.strip() != old_text)   
    
    allure.step("метод перемещения элемента в зону конструктора")
    def drag_and_drop_mouse(self, source, target):
        
        self.driver.execute_script("""
            function triggerDragAndDrop(dragElem, dropElem) {
                function createEvent(typeOfEvent) {
                    var event = document.createEvent("CustomEvent");
                    event.initCustomEvent(typeOfEvent, true, true, null);
                    event.dataTransfer = {
                        data: {},
                        setData: function (key, value) {
                            this.data[key] = value;
                        },
                        getData: function (key) {
                            return this.data[key];
                        }
                    };
                    return event;
                }

                function dispatchEvent(element, event, transferData) {
                    if (transferData !== undefined) {
                        event.dataTransfer = transferData;
                    }
                    if (element.dispatchEvent) {
                        element.dispatchEvent(event);
                    } else if (element.fireEvent) {
                        element.fireEvent("on" + event.type, event);
                    }
                }

                var dragStartEvent = createEvent('dragstart');
                dispatchEvent(dragElem, dragStartEvent);

                var dropEvent = createEvent('drop');
                dispatchEvent(dropElem, dropEvent, dragStartEvent.dataTransfer);

                var dragEndEvent = createEvent('dragend');
                dispatchEvent(dragElem, dragEndEvent, dropEvent.dataTransfer);
            }
            triggerDragAndDrop(arguments[0], arguments[1]);
        """, source, target)
    
    

