import pytest

from pages.categories_page import Categories_Page
from pages.computers_category import Categories_PC
from pages.corzina import Corzina
from pages.main_page import Main_Page
from pages.nouteboock_page import Nouteboocks_Page

def test1(start_client):

    # Определение классов переменных
    browser = start_client
    main_pages = Main_Page(browser)
    page_electro = Categories_Page(browser)
    categoriespc = Categories_PC(browser)
    reference_nout = Nouteboocks_Page(browser)
    page_corzina = Corzina(browser)

    # Покупка товара
    main_pages.start_main_page()
    page_electro.click_page_nouteboockes()
    categoriespc.start_computers_nouteboock()
    reference_nout.reference_noutebooc()
    page_corzina.start_corzina()
