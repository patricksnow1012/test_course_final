from selenium.webdriver.common.by import By
from base_class.base import Base

class Catalog(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Переменные
    reference_electronic = "(//a[@href = '/catalog--elektronika/54440'])[2]" #Навести на категорию Электроника
    filters_smartfone = "(//a[@class = 'egKyN _1mqvV _1wg9X'])[1]" #Кликнуть на категорию "Смартфоны"

    # Getters
    def send_reference_electronic(self):
        return self.browser.find_element(By.XPATH, self.reference_electronic)

    def send_filters_smartfone(self):
        return self.browser.find_element(By.XPATH, self.filters_smartfone)

    # Actions

    def click_filters_smartfone(self):
        self.send_filters_smartfone().click()

    # Steps

    def start_catalog(self):
        self.explicit_wait(self.reference_electronic, 5)
        self.hover_actions_chains(self.reference_electronic)
        self.on_time_sleep(3)
        self.click_filters_smartfone()
        self.on_time_sleep(3)
