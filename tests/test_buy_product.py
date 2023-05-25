# python -m pytest --alluredir=test_results/
# allure serve test_results/

import pytest
import allure
from pages.page_categories import PageCategories
from pages.page_categories_computers import PageChooseLaptop
from pages.page_basket import BasketPage
from pages.main_page import MainPage
from pages.page_laptop_list import PageLaptopList


@pytest.mark.run(order=1)
@allure.description('Покупка товара без авторизации')
def test_no_auth_buy_product(start_client):

    # Определение классов переменных

    browser = start_client
    main_page = MainPage(browser)
    categories_page = PageCategories(browser)
    laptop_reference_page = PageChooseLaptop(browser)
    laptop_list_page = PageLaptopList(browser)
    page_basket = BasketPage(browser)

    # Покупка товара без авторизации

    main_page.main_page_no_registration()  # Запуск главной страницы

    categories_page.start_click_laptop()  # Выбираю Компьютеры и Ноутбуки

    laptop_reference_page.start_choose_laptop()  # Выбираю ноутбуки

    laptop_list_page.start_buy_laptop()  # Покупаю ноутбук

    page_basket.start_compare_price_laptop()  # Сравниваю стоимость ноутбука
