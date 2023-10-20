import time
import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestQuatro():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_quatro(self):
        # Переходим по адресу
        self.driver.get("http://51.250.72.5:8094/login")

        # Установка размера окна
        self.driver.set_window_size(1389, 875)

        #  Открытие выпадающего списка
        element = self.driver.find_element(By.ID, "username")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()

        element = self.driver.find_element(By.CSS_SELECTOR, ".MuiBackdrop-root")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()

        # Выбор логина "master-operator"
        self.driver.find_element(By.CSS_SELECTOR, "body").click()
        self.driver.find_element(By.CSS_SELECTOR, ".MuiMenuItem-root").click()

        # Активация поля "Пароль"
        self.driver.find_element(By.ID, "password").click()

        # Ввод пароля, например, "12345"
        self.driver.find_element(By.ID, "password").send_keys("12345")

        # Нажатие кнопки "Войти"
        self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root").click()
        time.sleep(5)

