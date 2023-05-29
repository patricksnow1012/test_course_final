import allure

from base_class.base import Base
from pages.locators import MainPageLocators
from utilities.logger import Logger


class MainPage(Base):

    # Getters

    def get_captcha_skip(self):
        return self.explicit_wait(MainPageLocators.captcha_skip, 5)

    def get_catalog_button(self):
        return self.explicit_wait(MainPageLocators.catalog_button, 20)

    def get_button_categories_computer(self):
        return self.explicit_wait(MainPageLocators.button_categories_computer, 10)

    # Actions

    def skip_captcha(self):
        while True:
            try:
                self.get_captcha_skip().click()
                print('Каптча уничтожена')
                break

            except:
                print('Каптча не найдена')
                break

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print('Кликнул на каталог')

    def click_button_categories(self):
        self.get_button_categories_computer().click()
        print('Перехожу в раздел компьютеров и ноутбуков')

    # Start Steps

    def main_page_no_registration(self):
        with allure.step('Запуск главной страницы. Клик по категориям товаров'):
            Logger.add_start_step(method='main_page_no_registration')
            self.skip_captcha()
            self.get_current_url()
            self.click_catalog_button()
            self.click_button_categories()
            Logger.add_end_step(url=self.browser.current_url, method='main_page_no_registration')
