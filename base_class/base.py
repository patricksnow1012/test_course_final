import datetime

class Base():

    def __init__(self, browser):
        self.browser = browser

    def get_current_url(self):
        get_url = self.browser.current_url
        print(f'Url = {get_url}')

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good Value Word")

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f'screenshot {now_date}.png'
        self.browser.save_screenshot('C:\\Users\\Panknotkaen\\AquaProjects\\test_project\\test_site\\screen\\' + name_screenshot)

    def assert_get_url(self, result):
        get_url = self.browser.current_url
        assert get_url == result
        print("Good URL")
