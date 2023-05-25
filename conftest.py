from selenium import webdriver
import time
import pytest
from selenium.webdriver import DesiredCapabilities, ActionChains
from selenium.webdriver.common.by import By


@pytest.fixture()
def start_client():
    print('\nТест запускается')
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["pageLoadStrategy"] = "none"
    browser = webdriver.Chrome(options=option, desired_capabilities=capabilities, executable_path=
    'C:\\Users\\Panknotkaen\\Desktop\\test_course_final\\chromedriver.exe')
    browser.maximize_window()
    browser.get('https://www.onlinetrade.ru/')
    yield browser
    time.sleep(5)
    print('\nТест завершается')
    browser.quit()
