import allure

from base_class.base import Base
from pages.locators import PageLaptopListLocators
from utilities.logger import Logger


class PageLaptopList(Base):

    name_global_product = ''
    price_global_product = ''

    # Getters

    def get_buy_button(self):
        return self.explicit_wait(PageLaptopListLocators.buy, 10)

    def get_name_text(self):
        private_name_product = self.explicit_wait(PageLaptopListLocators.name_object, 5)
        PageLaptopList.name_global_product = self.remove_suffix(private_name_product, '(53013EUS) (53013EUS)')
        print(f'Название товара: {PageLaptopList.name_global_product}')
        return PageLaptopList.name_global_product

    def get_price_text(self):
        private_price_product = self.explicit_wait(PageLaptopListLocators.price_object, 5)
        PageLaptopList.price_global_product = self.remove_suffix(private_price_product, ' ₽')
        print(f'Цена товара = {PageLaptopList.price_global_product}')
        return PageLaptopList.price_global_product

    def get_continue_buy_button(self):
        return self.explicit_wait(PageLaptopListLocators.continue_buy, 5)

    def get_basket_button(self):
        return self.explicit_wait(PageLaptopListLocators.basket, 5)

    def get_skip_registration_button(self):
        return self.explicit_wait(PageLaptopListLocators.skip_registration, 5)

    # Actions

    def click_buy_button(self):
        self.get_buy_button().click()
        print('Кликнул на кнопку покупки')

    def click_continue_buy_button(self):
        # Пришлось сделать через JS скрипт, потому что элемент напрочь
        # отказывался кликаться как положено...
        self.browser.execute_script("arguments[0].click();", self.get_continue_buy_button())
        print('Кликнул на кнопку "Продолжить покупки"')

    def click_basket_button(self):
        self.get_basket_button().click()
        print('Кликнул на Корзину')

    def click_skip_registration_button(self):
        self.get_skip_registration_button().click()
        print('Пропускаю регистрацию')

    # Start Steps

    def start_buy_laptop(self):
        with allure.step('Покупка ноутбука'):
            Logger.add_start_step(method='start_buy_laptop')
            self.get_current_url()
            self.scroll(0, 500)
            self.get_name_text()
            self.get_price_text()
            self.click_buy_button()
            self.click_continue_buy_button()
            self.scroll(500, 0)
            self.click_basket_button()
            self.click_skip_registration_button()
            Logger.add_end_step(url=self.browser.current_url, method='start_buy_laptop')
