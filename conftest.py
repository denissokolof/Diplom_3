import pytest
from selenium import webdriver


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    driver = getattr(webdriver, browser.capitalize())()  
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()