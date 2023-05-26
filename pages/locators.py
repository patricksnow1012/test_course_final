from selenium.webdriver.common.by import By


# Локаторы главной страницы

class MainPageLocators:
    captcha_skip = (By.XPATH, "//input[@title = 'Вернуться на сайт']")
    catalog_button = (By.XPATH, "//a[contains(@class, 'header__buttonCatalog')]")
    button_categories_computer = (By.XPATH, "//span[contains(text(), 'Компьютеры')]")


# Локаторы страницы категорий товаров

class PageCategoriesLocators:
    laptop_reference = (By.XPATH, "//span[@class = 'drawCats__item__name'][contains(text(), 'Компьютеры и ноутбуки ')]")


# Локаторы страницы компьютерной техники

class PageCategoriesComputersLocators:
    choose_laptop = (By.XPATH, "//a[contains(@title, 'Ноутбуки')]")


# Локаторы страницы товаров ноутбуков

class PageLaptopListLocators:
    buy = (By.XPATH, "//a[contains(@title, 'HUAWEI MateBook D16')][contains(@class, 'button')]")
    name_object = (By.XPATH, "//a[contains(@class, 'item__name__3lines')][contains(@title, 'HUAWEI MateBook D16')]")
    price_object = (By.XPATH, "(//div[@class='indexGoods__item__price'])[4]")
    continue_buy = (By.XPATH, "//a[@class = ' js__popup__close']")
    basket = (By.XPATH, "//a[contains(@title, 'Товаров в корзине')]")
    skip_registration = (By.XPATH, "//a[@title = 'Продолжить без регистрации']")


# Локаторы страницы "Корзина"

class PageBasketLocators:
    finish_product_name = (By.XPATH, "//a[contains(@class, 'semibold') and contains(@title, 'Ноутбук HUAWEI')]")
    finish_product_price = (By.XPATH, "//div[@class = 'descriptionLine']/b[1]")
    finish_price_end = (By.XPATH, "//div[contains(@class, 'resultsLine')]/b")
