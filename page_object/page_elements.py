from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.locators import Locator


class PageElements:
    wait_time_out = 5

    def __init__(self, driver):
        self.driver = driver
        self.wait_variable = WebDriverWait(self.driver, self.wait_time_out)

    def get_game_name(self):
        game_name = self.wait_variable.until(
            expected_conditions.presence_of_element_located((By.TAG_NAME, Locator.header)))
        if game_name.is_displayed() is True:
            print(game_name.text)
        try:
            assert game_name.text == 'Grand Prix Hero'
        except AssertionError:
            print('Game name is invalid')
        return game_name

    def get_play_button(self):
        play_button = self.wait_variable.until(
            expected_conditions.presence_of_element_located((By.XPATH, Locator.play_button)))
        if play_button.is_displayed() is True:
            print(play_button.text)
        try:
            assert play_button.text == 'Ok, Play Now!'
        except AssertionError:
            print('Play button is invalid')
        return play_button