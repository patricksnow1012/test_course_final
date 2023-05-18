import pytest

from pages.catalog import Catalog
from pages.main_page import Main_Page

@pytest.mark.run(order=1)
def test1(start_client):

    browser = start_client

    main_pages = Main_Page(browser)
    main_pages.start_main_page()

    catalog_page = Catalog(browser)
    catalog_page.start_catalog()
