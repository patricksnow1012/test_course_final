from base_class.base import Base
from pages.nouteboock_page import Nouteboocks_Page

class Main_Page(Base):

    # Переменные

    price = "//div[@class = 'descriptionLine']/b[1]"
    catalog_itogo = "//a[contains(@class, 'semibold') and contains(@title, 'Ноутбук HUAWEI')]"
    itogo_price = "//div[contains(@class, 'resultsLine')]/b"

    #Getters

    def send_price(self):
        return self.explicit_wait(self.price, 5)

    def send_towar_name(self):
        return self.explicit_wait(self.catalog_itogo, 5)

    def send_itogo_price(self):
        return self.explicit_wait(self.itogo_price, 5)

    # Actions

    def read_price(self):
        self.convert_text(self.send_price())

    def read_name_towar(self):
        self.convert_text(self.send_towar_name())

    def read_final_price(self):
        self.convert_text(self.send_itogo_price())

    # Start Steps

    def start_main_page(self):
        self.get_current_url()
