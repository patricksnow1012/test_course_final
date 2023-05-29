import allure

from base_class.base import Base
from pages.locators import PageCategoriesComputersLocators
from utilities.logger import Logger


class PageChooseLaptop(Base):

    # Getters

    def get_choose_laptop(self):
        return self.explicit_wait(PageCategoriesComputersLocators.choose_laptop, 10)

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
