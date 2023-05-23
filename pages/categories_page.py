from selenium.webdriver.common.by import By

from base_class.base import Base

class Categories_Page(Base):

    # Переменные

    computers_nouteboock = "//span[@class = 'drawCats__item__name'][contains(text(), 'Компьютеры и ноутбуки ')]"

    # Getters

    def send_computers(self):
        return self.explicit_wait(self.computers_nouteboock, 10)

    # Actions

    def click_computers(self):
        self.send_computers().click()
        print('Выбрал категорию компьютеров и ноутбуков')

    # Steps

    def click_page_nouteboockes(self):
        self.get_current_url()
        self.click_computers()
