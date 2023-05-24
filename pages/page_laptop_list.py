from selenium.webdriver.common.by import By
from base_class.base import Base

class Page_laptop_list(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    name_global_product = str('')
    name_price_product = str('')

    # Variables

    buy = "//a[contains(@title, 'HUAWEI MateBook D16')][contains(@class, 'button')]"  #
    name_object = "//a[contains(@class, 'item__name__3lines')][contains(@title, 'HUAWEI MateBook')]"  #
    price_object = "//span[contains(text(), '75 900')]"
    continue_buy = "//a[@class = ' js__popup__close']"
    basket = "//a[contains(@title, 'Товаров в корзине')]"
    skip_registration = "//a[@title = 'Продолжить без регистрации']"

    # Getters

    def get_buy_button(self):
        return self.explicit_wait(self.buy, 20)

    def get_name_text(self):
        global name_global_product
        private_name_product = self.browser.find_element(By.XPATH, self.name_object)
        name_global_product = private_name_product.text.removesuffix('(53013EUS) (53013EUS)')
        print(f'Название товара: {name_global_product}')
        return name_global_product

    def get_price_text(self):
        global name_price_product
        private_price_product = self.browser.find_element(By.XPATH, self.price_object)
        name_price_product = private_price_product.text.removesuffix(' ₽')
        print(f'Цена товара = {name_price_product}')
        return name_price_product

    def get_continue_buy_button(self):
        return self.explicit_wait(self.continue_buy, 5)

    def get_basket_button(self):
        return self.explicit_wait(self.basket, 5)

    def get_skip_registration_button(self):
        return self.explicit_wait(self.skip_registration, 5)

    # Actions

    def click_buy_button(self):
        self.get_buy_button().click()
        print('Кликнул на кнопку покупки')

    def click_continue_buy_button(self):
        # Пришлось сделать через JS скрипт, потому что элемент напрочь
        # отказывался кликаться как положено...
        self.browser.execute_script("arguments[0].click();", self.get_continue_buy_button())
        print('Кликнул на кнопку "Продолжить покупки"')

    def click_basket_button(self):
        self.get_basket_button().click()
        print('Кликнул на Корзину')

    def click_skip_registration_button(self):
        self.get_skip_registration_button().click()
        print('Пропускаю регистрацию')

    # Start Steps

    def start_buy_laptop(self):
        self.get_current_url()
        self.scroll(0, 500)
        self.get_name_text()
        self.get_price_text()
        self.click_buy_button()
        self.click_continue_buy_button()
        self.scroll(500, 0)
        self.click_basket_button()
        self.click_skip_registration_button()
