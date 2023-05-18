from selenium.webdriver.common.by import By

from base_class.base import Base

class Formalization(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Переменные

    point_of_issue = "//input[@name = 'delivery-type-selector-DELIVERY-global']"
    input_address = "//*[@id='textfield4788108219']"
    apartment = "//*[@id='textfield8526232130']"
    floor = "//*[@id='textfield6767301205']"
    entrance = "//*[@id='textfield4656879447']"
    intercom = "//*[@id='textfield4622280437']"
    continues_offer = "/html/body/div[2]/div[2]/div/div[4]/div/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/div[2]/button[2]/span"

    # Getters

    def send_point_of_issue(self):
        return self.browser.find_element(By.XPATH, self.point_of_issue)

    def send_input_address(self):
        return self.browser.find_element(By.XPATH, self.input_address)

    def send_apartment(self):
        return self.browser.find_element(By.XPATH, self.apartment)

    def send_floor(self):
        return self.browser.find_element(By.XPATH, self.floor)

    def send_entrance(self):
        return self.browser.find_element(By.XPATH, self.entrance)

    def send_intercom(self):
        return self.browser.find_element(By.XPATH, self.intercom)

    def send_continues_offer(self):
        return self.browser.find_element(By.XPATH, self.continues_offer)

