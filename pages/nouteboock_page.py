import time

from selenium.webdriver.common.by import By

from base_class.base import Base

class Nouteboocks_Page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    i_name = str('')
    i_price = str('')

    # Переменные

    buy = "//a[contains(@title, 'HUAWEI MateBook D16')][contains(@class, 'button')]" #
    name_object = "//a[contains(@class, 'item__name__3lines')][contains(@title, 'HUAWEI MateBook')]" #
    price_object = "//span[contains(text(), '75 900')]"
    continue_buy = "//a[@class = ' js__popup__close']"
    corzina = "//a[contains(@title, 'Товаров в корзине')]"
    cont_noreg = "//a[@title = 'Продолжить без регистрации']"

    #Getters

    def send_buy(self):
        return self.explicit_wait(self.buy, 20)

    def send_name_object(self):
        global i_name
        name_towar = self.browser.find_element(By.XPATH, self.name_object)
        i_name = name_towar.text.removesuffix('(53013EUS) (53013EUS)')
        print(i_name)
        return i_name

    def send_price_object(self):
        global i_price
        price_towar = self.browser.find_element(By.XPATH, self.price_object)
        i_price = price_towar.text.removesuffix(' ₽')
        print(i_price)
        return i_price

    def send_continue_buy(self):
        return self.explicit_wait(self.continue_buy, 5)

    def send_corzina(self):
        return self.explicit_wait(self.corzina, 5)

    def send_cont_noreg(self):
        return self.explicit_wait(self.cont_noreg, 5)


    # Actions

    def click_buy(self):
        self.send_buy().click()

    def click_continue_buy(self):
        self.send_continue_buy().click()

    def click_corzina(self):
        self.send_corzina().click()

    def click_noreg(self):
        self.send_cont_noreg().click()

    # Start Steps

    def reference_noutebooc(self):
        self.get_current_url()
        self.scroll(0, 500)
        self.send_name_object()
        self.send_price_object()
        self.click_buy()
        self.click_continue_buy()
        self.scroll(500, 0)
        self.click_corzina()
        self.click_noreg()
