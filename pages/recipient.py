from selenium.webdriver.common.by import By
import pytest

from base_class.base import Base

class Recipient(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Переменные


    # Getters

    def send_first_and_last_name(self):
        return self.browser.find_element(By.XPATH, self.first_and_last_name)

    def send_email_address(self):
        return self.browser.find_element(By.XPATH, self.email_address)

    def send_mobile_number(self):
        return self.browser.find_element(By.XPATH, self.mobile_number)