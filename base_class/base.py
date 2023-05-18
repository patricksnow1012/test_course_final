import datetime
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, browser):
        self.browser = browser

    def explicit_wait(self, elements, sec):
        return WebDriverWait(self.browser, sec).until(
        EC.element_to_be_clickable((By.XPATH, elements)))

    def on_time_sleep(self, sec):
        return time.sleep(sec)

    def hover_actions_chains(self, element):
        locator = self.browser.find_element(By.XPATH, element)
        return ActionChains(self.browser).move_to_element(locator).perform()

    def get_current_url(self):
        get_url = self.browser.current_url
        print(f'Url = {get_url}')

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good Value Word")

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f'screenshot {now_date}.png'
        self.browser.save_screenshot('C:\\Users\\Panknotkaen\\AquaProjects\\test_project\\test_site\\screen\\' + name_screenshot)

    def assert_get_url(self, result):
        get_url = self.browser.current_url
        assert get_url == result
        print("Good URL")
