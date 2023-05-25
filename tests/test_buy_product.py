# python -m pytest --alluredir=test_results/
# allure serve test_results/

import pytest
import allure
from pages.page_categories import Page_categories
from pages.page_categories_computers import Page_choose_laptop
from pages.page_basket import Basket_page
from pages.main_page import Main_page
from pages.page_laptop_list import Page_laptop_list


@pytest.mark.run(order=1)
@allure.description('Покупка товара без авторизации')
def test_no_auth_buy_product(start_client):

    # Определение классов переменных

    browser = start_client
    main_page = Main_page(browser)
    categories_page = Page_categories(browser)
    laptop_reference_page = Page_choose_laptop(browser)
    laptop_list_page = Page_laptop_list(browser)
    page_basket = Basket_page(browser)

    # Покупка товара без авторизации

    main_page.main_page_no_registration()  # Запуск главной страницы

    categories_page.start_click_laptop()  # Выбираю Компьютеры и Ноутбуки

    laptop_reference_page.start_choose_laptop()  # Выбираю ноутбуки

    laptop_list_page.start_buy_laptop()  # Покупаю ноутбук

    page_basket.start_compare_price_laptop()  # Сравниваю стоимость ноутбука
