import time

from selenium.webdriver.common.by import By

from base_class.base import Base

class Nouteboocks_Page(Base):

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
        return self.explicit_wait(self.name_object, 10)

    def send_price_object(self):
        return self.explicit_wait(self.price_object, 10)

    def send_continue_buy(self):
        return self.explicit_wait(self.continue_buy, 5)

    def send_corzina(self):
        return self.explicit_wait(self.corzina, 5)

    def send_cont_noreg(self):
        return self.explicit_wait(self.cont_noreg, 5)


    # Actions

    def click_buy(self):
        self.send_buy().click()

    def read_name_object(self):
        self.convert_text(self.send_name_object())

    def read_price_object(self):
        self.convert_text(self.send_price_object())

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
        self.read_name_object()
        self.read_price_object()
        self.click_buy()
        self.click_continue_buy()
        self.refresh()
        self.scroll(500, 0)
        self.click_corzina()
        self.click_noreg()
