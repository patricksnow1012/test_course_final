from selenium.webdriver.common.by import By

from base_class.base import Base

class Categories_PC(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Переменные

    noutebock = "//a[contains(@title, 'Ноутбуки')]"

    # Getters

    def send_nouteboock_card(self):
        return self.explicit_wait(self.noutebock, 10)

    # Actions

    def click_nouteboock(self):
        self.send_nouteboock_card().click()
        print('Выбрал раздел Ноутбуков')

    # Steps

    def start_computers_nouteboock(self):
        self.get_current_url()
        self.click_nouteboock()
