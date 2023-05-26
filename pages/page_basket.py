import allure

from base_class.base import Base
from pages.locators import PageBasketLocators
from pages.page_laptop_list import PageLaptopList
from utilities.logger import Logger


class BasketPage(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    finish_global_name = ''
    finish_global_price = ''
    finish_price_global_end = ''

    # Getters

    def get_finish_name(self):
        finish_private_name = self.explicit_wait(PageBasketLocators.finish_product_name, 5)
        BasketPage.finish_global_name = self.remove_all_presuffix(finish_private_name, 'Ноутбук ',
                                                                   '(53013EUS) (53013EUS)')
        print(f'Наименование товара в корзине: {BasketPage.finish_global_name}')
        return BasketPage.finish_global_name

    def get_finish_price(self):
        finish_private_price = self.explicit_wait(PageBasketLocators.finish_product_price, 5)
        BasketPage.finish_global_price = self.remove_suffix(finish_private_price, ' ₽')
        print(f'Стоимость товара в корзине = {BasketPage.finish_global_price}')
        return BasketPage.finish_global_price

    def get_finish_price_end(self):
        finish_price_private_end = self.explicit_wait(PageBasketLocators.finish_price_end, 5)
        BasketPage.finish_price_global_end = self.remove_suffix(finish_price_private_end, ' ₽')
        print(f'Итоговая стоимость товара: {BasketPage.finish_price_global_end}')
        return BasketPage.finish_price_global_end

    # Start Steps

    def start_compare_price_laptop(self):
        with allure.step('Сравнение стоимости товара в корзине'):
            Logger.add_start_step(method='start_compare_price_laptop')
            self.get_current_url()
            self.get_finish_name()
            self.get_finish_price()
            self.scroll(0, 100)
            self.get_finish_price_end()
            self.assert_word(BasketPage.finish_global_name, PageLaptopList.name_global_product)
            self.assert_price(BasketPage.finish_global_price, PageLaptopList.price_global_product)
            self.assert_price(BasketPage.finish_price_global_end, PageLaptopList.price_global_product)
            self.get_screenshot()
            Logger.add_end_step(url=self.browser.current_url, method='start_compare_price_laptop')
