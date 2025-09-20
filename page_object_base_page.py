import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Класс главная страница
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def click(self, locator):
        return self.driver.find_element(*locator).click()
    
    def wait_for_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_any_elements_located(locator))
    
    def wait_clicable_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    
    def wait_invis_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
    
    def wait_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def current_url(self):
        return self.driver.current_url
    
    def wait_text_change(self, locator, old_text, timeout=30):
        WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element(*locator).text.strip() != old_text)   
    
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
    
    

