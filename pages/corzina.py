from pages.nouteboock_page import Nouteboocks_Page

class Corzina(Nouteboocks_Page):

    # Переменные

    price = "//div[@class = 'descriptionLine']/b[1]"
    towar_name = "//a[contains(@class, 'semibold') and contains(@title, 'Ноутбук HUAWEI')]"
    itogo_price = "//div[contains(@class, 'resultsLine')]/b"

    #Getters

    def send_price(self):
        return self.explicit_wait(self.price, 5)

    def send_towar_name(self):
        return self.explicit_wait(self.towar_name, 5)

    def send_itogo_price(self):
        return self.explicit_wait(self.itogo_price, 5)

    # Actions

    def read_price(self):
        self.remove_suffix(self.send_price(), ' ₽')

    def read_name_towar(self):
        self.remove_suffix(self.send_towar_name(), '(53013EUS) (53013EUS)')

    def read_final_price(self):
        self.remove_suffix(self.send_itogo_price(), ' ₽')

    # Start Steps

    def start_corzina(self):
        self.get_current_url()
        self.scroll(0, 500)
        assert self.read_price() == self.read_price_object(), 'Invalid price'
