# Cross-Browser Test Using POM as Locators.
import random
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ZoryanaPleskun.UnittestLC import Locators
import Locators as Lc


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.set_window_size(1120, 550)
        driver.get(Lc.main_url)
        wait = WebDriverWait(driver, 3)

        driver.find_element(By.XPATH, Lc.logo).click()
        driver.find_element(By.XPATH, Lc.seller).click()

        try:
            driver.find_element(By.XPATH, Lc.banner)
            print("is VISIBLE")
        except NoSuchElementException:
            print("is not VISIBLE")

        driver.find_element(By.XPATH, Lc.search_field).click()
        driver.find_element(By.XPATH, Lc.search_field).send_keys("Table")
        driver.find_element(By.XPATH, Lc.search_submit).click()
        wait = WebDriverWait(driver, 3)


class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.set_window_size(1120, 550)
        driver.get(Lc.main_url)
        wait = WebDriverWait(driver, 3)

        driver.find_element(By.XPATH, Lc.logo).click()
        driver.find_element(By.XPATH, Lc.seller).click()

        try:
            driver.find_element(By.XPATH, Lc.banner)
            print("is VISIBLE")
        except NoSuchElementException:
            print("is not VISIBLE")

        driver.find_element(By.XPATH, Lc.search_field).click()
        driver.find_element(By.XPATH, Lc.search_field).send_keys("Table")
        driver.find_element(By.XPATH, Lc.search_submit).click()
        wait = WebDriverWait(driver, 3)

    def tearDown(self):
        self.driver.quit()
