from selenium.webdriver.common.by import By
from base_class.base import Base
from pages.page_laptop_list import Page_laptop_list


class Basket_page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    finish_global_price = ''
    finish_global_name = ''
    finish_price_global_end = ''

    # Variables

    finish_product_price = "//div[@class = 'descriptionLine']/b[1]"
    finish_product_name = "//a[contains(@class, 'semibold') and contains(@title, 'Ноутбук HUAWEI')]"
    finish_price_end = "//div[contains(@class, 'resultsLine')]/b"

    # Getters

    def get_finish_price(self):
        finish_private_price = self.browser.find_element(By.XPATH, self.finish_product_price)
        Basket_page.finish_global_price = finish_private_price.text.removesuffix(' ₽')
        print(f'Стоимость товара в корзине = {Basket_page.finish_global_price}')
        return Basket_page.finish_global_price

    def get_finish_name(self):
        finish_private_name = self.browser.find_element(By.XPATH, self.finish_product_name)
        Basket_page.finish_global_name = finish_private_name.text.removesuffix('(53013EUS) (53013EUS)')
        print(f'Наименование товара в корзине: {Basket_page.finish_global_name}')
        return Basket_page.finish_global_name

    def get_finish_price_end(self):
        finish_price_private_end = self.browser.find_element(By.XPATH, self.finish_price_global_end)
        Basket_page.finish_price_global_end = finish_price_private_end.text.removesuffix(' ₽')
        print(f'Итоговая стоимость товара: {Basket_page.finish_price_global_end}')
        return Basket_page.finish_price_global_end

    # Start Steps

    def start_compare_price_laptop(self):
        self.scroll(0, 500)
        self.get_current_url()
        self.get_finish_name()
        self.get_finish_price()
        print(Page_laptop_list.name_price_product)
        self.assert_word(Page_laptop_list.name_price_product, self.get_finish_price)
        self.get_screenshot()
