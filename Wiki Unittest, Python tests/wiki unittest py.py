import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def test_search(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org/")

        def delay():
            time.sleep(random.randint(1, 3))

            driver.find_element(By.XPATH, '//*[@class="central-featured-logo"]')
            print(driver.find_element(By.XPATH,
                                      "//strong[contains(text(),'The Free Encyclopedia')]").get_attribute(
                "href"))

            assert "Wikipedia" in driver.title
            print(driver.title)

            driver.find_element(By.XPATH, "//input[@id='searchInput']").click()
            driver.find_element(By.XPATH, "//input[@id='searchInput']").send_keys("bread")
            driver.find_element(By.XPATH, "//i[contains(text(),'Search')]").click()
            delay()
            driver.find_element(By.XPATH, "//*[@alt='Loaves of bread in a basket']").click()
            delay()
            # driver.find_element(By.XPATH, "//*[@class='mw-mmv-final-image jpg']").send_keys()
            # delay()
            driver.find_element(By.XPATH, "//*[@class='mw-mmv-next-image']").send_keys()
            delay()
            driver.find_element(By.XPATH, "//*[@class='mw-mmv-close']").click()
            delay()


            try:
                driver.find_element(By.XPATH, "//*[@class='mw-mmv-final-image jpg']")
                print("is VISIBLE")
            except NoSuchElementException:
                print("is not VISIBLE")

    def test_search_chrome_1120x850(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org/")

        def delay():
            time.sleep(random.randint(1, 3))

            driver.find_element(By.XPATH, '//*[@class="central-featured-logo"]')
            print(driver.find_element(By.XPATH,
                                      "//strong[contains(text(),'The Free Encyclopedia')]").get_attribute(
                "href"))

            assert "Wikipedia" in driver.title
            print(driver.title)

            driver.find_element(By.XPATH, "//input[@id='searchInput']").click()
            driver.find_element(By.XPATH, "//input[@id='searchInput']").send_keys("bread")
            driver.find_element(By.XPATH, "//i[contains(text(),'Search')]").click()
            delay()
            driver.find_element(By.XPATH, "//*[@alt='Loaves of bread in a basket']").click()
            delay()
            # driver.find_element(By.XPATH, "//*[@class='mw-mmv-final-image jpg']").send_keys()
            # delay()
            driver.find_element(By.XPATH, "//*[@class='mw-mmv-next-image']").send_keys()
            delay()
            driver.find_element(By.XPATH, "//*[@class='mw-mmv-close']").click()
            delay()

    def tearDown(self):
        self.driver.quit()


class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org/")

        def delay():
            time.sleep(random.randint(1, 3))
            driver.find_element(By.XPATH, '//*[@class="central-featured-logo"]')
            print(driver.find_element(By.XPATH,
                                      "//strong[contains(text(),'The Free Encyclopedia')]").get_attribute(
                "href"))

            assert "Wikipedia" in driver.title
            print(driver.title)

            driver.find_element(By.XPATH, "//input[@id='searchInput']").click()
            driver.find_element(By.XPATH, "//input[@id='searchInput']").send_keys("bread")
            driver.find_element(By.XPATH, "//i[contains(text(),'Search')]").click()
            delay()
            driver.find_element(By.XPATH, "//*[@alt='Loaves of bread in a basket']").click()
            delay()
            # driver.find_element(By.XPATH, "//*[@class='mw-mmv-final-image jpg']").send_keys()
            # delay()
            driver.find_element(By.XPATH, "//*[@class='mw-mmv-next-image']").send_keys()
            delay()
            driver.find_element(By.XPATH, "//*[@class='mw-mmv-close']").click()
            delay()

            try:
                driver.find_element(By.XPATH, "//*[@class='mw-mmv-final-image jpg']")
                print("is VISIBLE")
            except NoSuchElementException:
                print("is not VISIBLE")

    def test_search_edge_1120x850(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org/")

        def delay():
            time.sleep(random.randint(1, 3))

            driver.find_element(By.XPATH, '//*[@class="central-featured-logo"]')
            print(driver.find_element(By.XPATH,
                                      "//strong[contains(text(),'The Free Encyclopedia')]").get_attribute(
                "href"))

            assert "Wikipedia" in driver.title
            print(driver.title)

            driver.find_element(By.XPATH, "//input[@id='searchInput']").click()
            driver.find_element(By.XPATH, "//input[@id='searchInput']").send_keys("bread")
            driver.find_element(By.XPATH, "//i[contains(text(),'Search')]").click()
            delay()
            driver.find_element(By.XPATH, "//*[@alt='Loaves of bread in a basket']").click()
            delay()
            # driver.find_element(By.XPATH, "//*[@class='mw-mmv-final-image jpg']").send_keys()
            # delay()
            driver.find_element(By.XPATH, "//*[@class='mw-mmv-next-image']").send_keys()
            delay()
            driver.find_element(By.XPATH, "//*[@class='mw-mmv-close']").click()
            delay()

    def tearDown(self):
        self.driver.quit()


