from selenium.webdriver.common.by import By

from base_class.base import Base

class Main_Page(Base):

    # Переменные

    catalog_button = "//button[@id = 'catalogPopupButton']"
    captcha_huyatcha = "//input[@id='js-button']"
    elementik = "//span[text() = 'Выгодно']"

    #Getters

    def send_catalog_button(self):
        return self.browser.find_element(By.XPATH, self.catalog_button)

    def send_captcha_huyatcha(self):
        return self.browser.find_element(By.XPATH, self.captcha_huyatcha)

    # Actions

    def click_catalog_button(self):
        while True:
            try:
                self.send_catalog_button().click()
                print('Кликнул на каталог товаров')
                break
            except:
                self.send_catalog_button().click()
                print('Кликнул на каталог товаров')
                break

    def click_send_captcha(self):
        while True:
            try:
                self.send_captcha_huyatcha().click()
                break
            except:
                break

    # Start Steps

    def start_main_page(self):
        self.click_send_captcha()
        self.get_current_url()
        self.explicit_wait(self.catalog_button, 5)
        self.click_catalog_button()
