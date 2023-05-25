import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:

    # Инициализация браузера
    def __init__(self, browser):
        self.browser = browser

    # Обновление страницы
    def refresh_page(self):
        return self.browser.refresh()

    # Удаление префикса и суффикса

    def remove_all_presuffix(self, element, prefix, suffix):
        element = element.text.removeprefix(f'{prefix}').removesuffix(f'{suffix}')
        return element

    # Конвертирование элемента в текст + удаление суффикса

    def remove_suffix(self, element, suffix):
        element = element.text.removesuffix(f'{suffix}')
        return element

    # Конвертирование элемента в текст + удаление префикса

    def remove_prefix(self, element, prefix):
        element = element.text.removeprefix(f'{prefix}')
        return element

    # Неявное ожидание
    def implicitly_waits(self, seconds):
        return self.browser.implicitly_wait(seconds)

    # Явное ожидание
    def explicit_wait(self, elements, sec):
        return WebDriverWait(self.browser, sec).until(
            EC.element_to_be_clickable((By.XPATH, elements)))

    # Скролл страницы
    def scroll(self, x, y):
        return self.browser.execute_script(f'window.scrollBy({x},{y})')

    # Time Sleep
    def on_time_sleep(self, sec):
        return time.sleep(sec)

    # Наведение на элемент
    def hover_actions_chains(self, element):
        locator = self.browser.find_element(By.XPATH, element)
        return ActionChains(self.browser).move_to_element(locator).perform()

    # Получение урл текущей страницы
    def get_current_url(self):
        get_url = self.browser.current_url
        print(f'Текущий URL = {get_url}')

    # Проверка текста
    def assert_word(self, word, result):
        assert word == result
        print("Названия товаров совпадают!")

    def assert_price(self, price1, price2):
        assert price1 == price2
        print("Стоимость товаров совпадает!")


    # Скриншот
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f'screenshot {now_date}.png'
        self.browser.save_screenshot('C:\\Users\\Panknotkaen\\AquaProjects\\test_project\\test_site\\screen\\'
                                     + name_screenshot)

    # Проверка урл
    def assert_get_url(self, result):
        get_url = self.browser.current_url
        assert get_url == result
        print("Good URL")
