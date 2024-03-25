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
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, 'img[id="treasure"]')
    x = x_element.get_attribute('valuex')
    logging.info(f'Получение х: {x}')
    y = calc(x)
    logging.info(f'Расчетное значение y: {y}')
    logging.info(f'Вставка ответа')
    input_space = browser.find_element(By.CSS_SELECTOR,'input[id="answer"]')
    input_space.send_keys(y)
    logging.info(f'Выбор чекбока')
    cheq_box = browser.find_element(By.CSS_SELECTOR,'[id="robotCheckbox"]')
    # logging.info(f'Выбран чекбокс - {cheq_box.text}')
    cheq_box.click()
    logging.info(f'Выбор радиобатон')
    rad_box = browser.find_element(By.CSS_SELECTOR, 'input[id="robotsRule"]')
    rad_box.click()
    logging.info(f'Отправка ответа')
    button = browser.find_element(By.CSS_SELECTOR,'button.btn[type="submit"]')
    button.click()

finally:
    logging.info(f'Успех')
    time.sleep(30)
    browser.quit()