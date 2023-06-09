from selenium import webdriver
import time
import pytest
from selenium.webdriver import DesiredCapabilities


@pytest.fixture()
def start_client():
    print('\nТест запускается')
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])  # Очистка консоли от мусора с ошибками
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["pageLoadStrategy"] = "eager"  # Чтобы не ждать долгую загрузку сайта
    browser = webdriver.Chrome(options=option, desired_capabilities=capabilities, executable_path=
    'C:\\Users\\Panknotkaen\\Desktop\\test_course_final\\chromedriver.exe')
    browser.maximize_window()
    browser.get('https://www.onlinetrade.ru/')
    yield browser
    time.sleep(5)
    print('\nТест завершается')
    browser.quit()
