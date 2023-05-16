from selenium.webdriver.common.by import By
import pytest

from base_class.base import Base

class Alert_Buy(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser


    # Переменные

    continue_buy = "/html/body/div[21]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/button/span"

    # Getters
    def send_continue_buy(self):
        return self.browser.find_element(By.XPATH, self.continue_buy)

