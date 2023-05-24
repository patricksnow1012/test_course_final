from selenium.webdriver.common.by import By
from base_class.base import Base
from pages.page_laptop_list import Page_laptop_list


class Basket_page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    finish_global_price = str('')
    finish_global_name = str('')
    finish_price_global_end = str('')

    # Variables

    finish_product_price = "//div[@class = 'descriptionLine']/b[1]"
    finish_product_name = "//a[contains(@class, 'semibold') and contains(@title, 'Ноутбук HUAWEI')]"
    finish_price_end = "//div[contains(@class, 'resultsLine')]/b"

    # Getters

    def get_finish_price(self):
        global finish_global_price
        end_price = self.browser.find_element(By.XPATH, self.finish_product_price)
        finish_global_price = end_price.text.removesuffix(' ₽')
        print(f'Стоимость товара = {finish_global_price}')
        return finish_global_price

    def get_finish_name(self):
        global finish_global_name
        end_name = self.browser.find_element(By.XPATH, self.finish_product_name)
        finish_global_name = end_name.text.removesuffix('(53013EUS) (53013EUS)')
        print(f'Наименование товара: {finish_global_name}')
        return finish_global_name

    def get_finish_price_end(self):
        global finish_price_global_end
        finish_end_price = self.browser.find_element(By.XPATH, self.finish_price_global_end)
        finish_price_global_end = finish_end_price.text.removesuffix(' ₽')
        print(f'Итоговая стоимость товара: {finish_price_global_end}')
        return finish_price_global_end

    # Start Steps

    def start_compare_price_laptop(self):
        self.get_current_url()
        self.scroll(0, 500)
        print(self.finish_global_price)
        print(Page_laptop_list.name_price_product)
        self.assert_word(Page_laptop_list.name_price_product, self.finish_global_price)
        self.get_screenshot()
