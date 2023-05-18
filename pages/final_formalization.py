from selenium.webdriver.common.by import By

from base_class.base import Base

class Final_formalization(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Переменные

    final_price = "/html/body/div[2]/div[2]/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[7]/div/div/span/span[1]"

    # Getters

    def send_final_price(self):
        return self.browser.find_element(By.XPATH, self.final_price)