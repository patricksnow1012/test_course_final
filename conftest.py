from selenium import webdriver
import time
import pytest
from selenium.webdriver import DesiredCapabilities


@pytest.fixture()
def start_client():
    option = webdriver.ChromeOptions()
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["pageLoadStrategy"] = "eager"
    browser = webdriver.Chrome(options=option, desired_capabilities=capabilities, executable_path=
                                        'C:\\Users\\Panknotkaen\\Desktop\\test_course_final\\chromedriver.exe')
    browser.maximize_window()
    browser.get('https://www.onlinetrade.ru/')
    yield browser
    time.sleep(5)
