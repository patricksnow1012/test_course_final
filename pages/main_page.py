from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from base_class.base import Base


class Main_Page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Переменные

    catalog_button = "//button[@id = 'catalogPopupButton']"