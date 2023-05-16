from selenium.webdriver.common.by import By
import pytest

from base_class.base import Base

class Smartfons(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Переменные

    iphone_list = "//*[contains(text(), 'iPhone')]"
    name_iphone = "/html/body/div[2]/div[2]/div[1]/div[5]/div/div/div/div/div/div/div[5]/div/div/div/div/main/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/article/div[1]/h3/a/span"
    price_iphone = "/html/body/div[2]/div[2]/div[1]/div[5]/div/div/div/div/div/div/div[5]/div/div/div/div/main/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/article/div[2]/div[1]/div/div/a/div/h3/span[2]"
    buy_iphone = "/html/body/div[2]/div[2]/div[1]/div[5]/div/div/div/div/div/div/div[5]/div/div/div/div/main/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/article/div[2]/div[4]/div/button"

    # Getters

    def send_iphone_list(self):
        return self.browser.find_element(By.XPATH, self.iphone_list)

    def send_name_iphone(self):
        return self.browser.find_element(By.XPATH, self.name_iphone)

    def send_price_iphone(self):
        return self.browser.find_element(By.XPATH, self.price_iphone)

    def send_buy_iphone(self):
        return self.browser.find_element(By.XPATH, self.buy_iphone)