from selenium.webdriver.common.by import By
import pytest

from base_class.base import Base

class Main_Page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Переменные

    catalog_button = "//button[@id = 'catalogPopupButton']"

    #Getters

    def send_catalog_button(self):
        return self.browser.find_element(By.XPATH, self.catalog_button)

    # Actions

    def click_catalog_button(self):
        self.send_catalog_button().click()
        print('Кликнул на каталог товаров')

    # Start Steps

    def start_main_page(self):
        self.get_current_url()
        self.click_catalog_button()

