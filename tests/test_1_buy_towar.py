from selenium import webdriver
import pytest

from pages.main_page import Main_Page

@pytest.mark.run(order=1)
def test1():

    browser = webdriver.Firefox()

    main_pages = Main_Page(browser)
    main_pages.start_main_page()
