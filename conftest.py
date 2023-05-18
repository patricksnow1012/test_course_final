from selenium import webdriver
import time
import pytest

@pytest.fixture()
def start_client():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get('https://market.yandex.ru/')
    yield browser
    time.sleep(3)
    browser.quit()
