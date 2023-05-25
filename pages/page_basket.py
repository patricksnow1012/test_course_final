import allure

from base_class.base import Base
from pages.page_laptop_list import Page_laptop_list
from utilities.logger import Logger


class Basket_page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    finish_global_name = ''
    finish_global_price = ''
    finish_price_global_end = ''

    # Variables

    finish_product_name = "//a[contains(@class, 'semibold') and contains(@title, 'Ноутбук HUAWEI')]"
    finish_product_price = "//div[@class = 'descriptionLine']/b[1]"
    finish_price_end = "//div[contains(@class, 'resultsLine')]/b"

    # Getters

    def get_finish_name(self):
        finish_private_name = self.explicit_wait(self.finish_product_name, 5)
        Basket_page.finish_global_name = self.remove_all_presuffix(finish_private_name, 'Ноутбук ',
                                                                   '(53013EUS) (53013EUS)')
        print(f'Наименование товара в корзине: {Basket_page.finish_global_name}')
        return Basket_page.finish_global_name

    def get_finish_price(self):
        finish_private_price = self.explicit_wait(self.finish_product_price, 5)
        Basket_page.finish_global_price = self.remove_suffix(finish_private_price, ' ₽')
        print(f'Стоимость товара в корзине = {Basket_page.finish_global_price}')
        return Basket_page.finish_global_price

    def get_finish_price_end(self):
        finish_price_private_end = self.explicit_wait(self.finish_price_end, 5)
        Basket_page.finish_price_global_end = self.remove_suffix(finish_price_private_end, ' ₽')
        print(f'Итоговая стоимость товара: {Basket_page.finish_price_global_end}')
        return Basket_page.finish_price_global_end

    # Start Steps

    def start_compare_price_laptop(self):
        with allure.step('Сравнение стоимости товара в корзине'):
            Logger.add_start_step(method='start_compare_price_laptop')
            self.get_current_url()
            self.get_finish_name()
            self.get_finish_price()
            self.scroll(0, 100)
            self.get_finish_price_end()
            self.assert_word(Basket_page.finish_global_name, Page_laptop_list.name_global_product)
            self.assert_price(Basket_page.finish_global_price, Page_laptop_list.price_global_product)
            self.assert_price(Basket_page.finish_price_global_end, Page_laptop_list.price_global_product)
            self.get_screenshot()
            Logger.add_end_step(url=self.browser.current_url, method='start_compare_price_laptop')
