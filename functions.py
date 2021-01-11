from selenium.webdriver.support.wait import WebDriverWait
from page_object.page_elements import PageElements


class Functions:
    wait_time_out = 5

    def __init__(self, driver):
        self.driver = driver
        self.wait_variable = WebDriverWait(self.driver, self.wait_time_out)

        self.base_url = 'https://www.minigames.com/games/grand-prix-hero'
        self.page_elements = PageElements(driver)

    def setup(self):
        self.driver.get(self.base_url)

    def game_name(self):
        self.page_elements.get_game_name()

