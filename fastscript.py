import random

import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
import pytest
import math
from seleniumbase import Driver

driver = Driver()
driver.get("https://selenium.dev")

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s [%(name)s]: %(message)s')

try:
    logging.info('Запуск скрипта')
    link = 'https://redmine.r77.center-inform.ru/issues/366111' #redmine
    browser = webdriver.Chrome()
    browser.get(link)

    input_loggin = browser.find_element(By.CSS_SELECTOR, 'input[id="confirmCode"]')
    input_loggin.send_keys(str(i))
    time.sleep(0.5)
    button_3 = browser.find_element(By.CSS_SELECTOR, 'button.accept-button')
    button_3.click()
    time.sleep(0.5)


    posts = browser.find_elements(By.CSS_SELECTOR, 'div.journal.has-notes.has-details')
    for post in posts:
        print(post.text())

finally:
    time.sleep(10)
    logging.info(f'Успех')
    browser.quit()