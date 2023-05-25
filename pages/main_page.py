import allure

from base_class.base import Base
from utilities.logger import Logger


class MainPage(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Variables

    captcha_skip = "//input[@title = 'Вернуться на сайт']"
    catalog_button = "//a[contains(@class, 'header__buttonCatalog')]"  #
    button_categories_computer = "//span[contains(text(), 'Компьютеры')]"  #

    # Getters

    def get_captcha_skip(self):
        return self.explicit_wait(self.captcha_skip, 5)

    def get_catalog_button(self):
        return self.explicit_wait(self.catalog_button, 20)

    def get_button_categories_computer(self):
        return self.explicit_wait(self.button_categories_computer, 10)

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
