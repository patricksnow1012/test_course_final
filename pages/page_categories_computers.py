import allure

from base_class.base import Base
from utilities.logger import Logger


class Page_choose_laptop(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Variables

    choose_laptop = "//a[contains(@title, 'Ноутбуки')]"

    # Getters

    def get_choose_laptop(self):
        return self.explicit_wait(self.choose_laptop, 10)

    # Actions

    def click_choose_laptop(self):
        self.get_choose_laptop().click()
        print('Выбрал раздел Ноутбуки')

    # Steps

    def start_choose_laptop(self):
        with allure.step('Выбрать категорию "Ноутбуки"'):
            Logger.add_start_step(method='start_choose_laptop')
            self.get_current_url()
            self.click_choose_laptop()
            Logger.add_end_step(url=self.browser.current_url, method='start_choose_laptop')
