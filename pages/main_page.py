from selenium.webdriver.common.by import By

from base_class.base import Base

class Main_Page(Base):

    # Переменные

    captcha = "//input[@title = 'Вернуться на сайт']"
    catalog = "//a[contains(@class, 'header__buttonCatalog')]" #
    categories_computer = "//span[contains(text(), 'Компьютеры')]" #

    #Getters

    def send_captcha(self):
        return self.explicit_wait(self.captcha, 5)

    def send_catalog(self):
        return self.explicit_wait(self.catalog, 20)

    def send_categories_computer(self):
        return self.explicit_wait(self.categories_computer, 10)

    # Actions

    def pas_captcha(self):
        while True:
            try:
                self.send_captcha().click()
                break
            except:
                break

    def click_electronics(self):
        self.send_catalog().click()
        print('Кликнул на каталог')

    def click_computers(self):
        self.send_categories_computer().click()
        print('Перехожу в раздел компьютеров и ноутбуков')

    # Start Steps

    def start_main_page(self):
        self.pas_captcha()
        self.get_current_url()
        self.click_electronics()
        self.click_computers()
