from selenium.webdriver.common.by import By
import pytest

from base_class.base import Base

class Catalog(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Переменные
    reference_electronic = "/html/body/div[22]/div[8]/div[1]/div/div/div/div/div/div/div[1]/div/ul/li[4]/a"
    filters_smartfone = "/html/body/div[22]/div[8]/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/ul/li[1]/div/a"

    # Getters
    def send_reference_electronic(self):
        return self.browser.find_element(By.XPATH, self.reference_electronic)

    def send_filters_smartfone(self):
        return self.browser.find_element(By.XPATH, self.filters_smartfone)

    # Actions
    def move_to_reference_electronic(self):


