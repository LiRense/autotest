import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
import pytest

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s [%(name)s]: %(message)s',
                    filename='tests.log', filemode='w')

def test_1():
    try:
        logging.info('Запуск первого Теста')
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_buttons = browser.find_elements(By.CSS_SELECTOR,'.form-group input:required')
        for id,input_button in enumerate(input_buttons):
            input_button.send_keys(id)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert welcome_text == "Congratulations! You have successfully registered!"
    except selenium.common.NoSuchElementException as NoSuchElementException:
        logging.error(NoSuchElementException, exc_info=True)
    finally:
        logging.info('Совпадение текста: '+'True')
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
        logging.info('Первый Тест завешен')


def test_2():
    try:
        logging.info('Запуск второго Теста')
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_buttons = browser.find_elements(By.CSS_SELECTOR,'.form-group input')
        for id,input_button in enumerate(input_buttons):
            input_button.send_keys(id)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert welcome_text == "Congratulations! You have successfully registered!"
    except selenium.common.NoSuchElementException as NoSuchElementException:
        logging.error(NoSuchElementException, exc_info=True)
    finally:
        logging.info('Совпадение текста: '+'True')
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
        logging.info('Второй Тест завешен')

def test_3():
    try:
        logging.info('Запуск третьего Теста')
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_buttons = browser.find_elements(By.CSS_SELECTOR,'.form-group input:not(:required)')
        for id,input_button in enumerate(input_buttons):
            input_button.send_keys(id)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert welcome_text == "Congratulations! You have successfully registered!"
    except selenium.common.NoSuchElementException as NoSuchElementException:
        logging.error(NoSuchElementException, exc_info=True)
    finally:
        logging.info('Совпадение текста: '+'True')
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
        logging.info('Третий Тест завершен')

