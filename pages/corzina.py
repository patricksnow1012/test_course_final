from selenium.webdriver.common.by import By

from base_class.base import Base
from pages.nouteboock_page import Nouteboocks_Page


class Corzina(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    finish_price = str('')
    finish_name = str('')
    finish_price_itogo = str('')

    # Переменные

    price = "//div[@class = 'descriptionLine']/b[1]"
    towar_name = "//a[contains(@class, 'semibold') and contains(@title, 'Ноутбук HUAWEI')]"
    itogo_price = "//div[contains(@class, 'resultsLine')]/b"

    #Getters

    def send_price(self):
        global finish_price
        end_price = self.browser.find_element(By.XPATH, self.price)
        finish_price = end_price.text.removesuffix(' ₽')
        print(finish_price)
        return finish_price

    def send_towar_name(self):
        global finish_name
        end_name = self.browser.find_element(By.XPATH, self.towar_name)
        finish_name = end_name.text.removesuffix('(53013EUS) (53013EUS)')
        print(finish_name)
        return finish_name

    def send_itogo_price(self):
        global finish_price_itogo
        finish_end_price = self.browser.find_element(By.XPATH, self.finish_price_itogo)
        finish_price_itogo = finish_end_price.text.removesuffix(' ₽')
        print(finish_price_itogo)
        return finish_price_itogo

    # Start Steps

    def start_corzina(self):
        self.get_current_url()
        self.scroll(0, 500)
        print(self.finish_price)
        print(Nouteboocks_Page.i_price)
        self.assert_word(Nouteboocks_Page.i_price, self.finish_price)
