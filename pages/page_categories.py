from base_class.base import Base


class Page_categories(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Variables

    laptop_reference = "//span[@class = 'drawCats__item__name'][contains(text(), 'Компьютеры и ноутбуки ')]"

    # Getters

    def get_laptop_reference(self):
        return self.explicit_wait(self.laptop_reference, 10)

    # Actions

    def click_laptop_reference(self):
        self.get_laptop_reference().click()
        print('Выбрал категорию компьютеров и ноутбуков')

    # Steps

    def start_click_laptop(self):
        self.get_current_url()
        self.click_laptop_reference()
