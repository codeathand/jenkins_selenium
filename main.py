import os

from selenium import webdriver

from functions import Functions

options = webdriver.chrome.options.Options()
options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-extensions")
options.add_argument('window-size=1920x1480')
driver = webdriver.Chrome(options=options)

PATH_FIREFOX = os.getcwd() + '\\drivers\\geckodriver-v0.28.0-win64\\geckodriver.exe'
PATH_CHROME = os.getcwd() + '\\drivers\\chromedriver_win32\\chromedriver.exe'

# base_url = 'https://www.marksandspencer.com/'

main_test_chrome = Functions(webdriver.Chrome(options=options))
main_test_chrome.setup()
main_test_chrome.game_name()
main_test_chrome.play_button()
