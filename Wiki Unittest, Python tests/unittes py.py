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
            driver.get("https://qasvus.wordpress.com")

            def delay():
                time.sleep(random.randint(1, 3))

            driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()
            print(driver.find_element(By.XPATH,
                                      '//*[@class="site-title"]//*[text()="California Real Estate"]').get_attribute(
                "href"))
            print(driver.find_element(By.XPATH,
                                      '//*[@class="wp-block-cover__image-background wp-image-54"]').get_attribute(
                "src"))

            assert "California Real Estate" in driver.title
            print(driver.title)

            driver.find_element(By.ID, "send-us-a-message")
            driver.find_element(By.ID, "g2-name").send_keys("Zoryana")
            driver.find_element(By.ID, "g2-email").send_keys('zoryana_ukraine@yahoo.com')
            driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys('Hi, How May I Help You?')
            driver.find_element(By.XPATH, '//*[@class="pushbutton-wide"]').click()
            delay()

            try:
                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "link")))
                print(" 'go back' link is VISIBLE")
            except TimeoutException:
                print("'go back' link is not VISIBLE")

            driver.find_element(By.CLASS_NAME, "link").click()
            print(driver.find_element(By.CLASS_NAME, "pushbutton-wide").get_attribute('type'))

    def test_search_chrome_1120x550(self):
        driver = self.driver
        driver.set_window_size(1120, 550)
        driver.get("https://qasvus.wordpress.com")

        def delay():
            time.sleep(random.randint(1, 3))

        driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()
        print(driver.find_element(By.XPATH,
                                  '//*[@class="site-title"]//*[text()="California Real Estate"]').get_attribute(
            "href"))
        print(driver.find_element(By.XPATH,
                                  '//*[@class="wp-block-cover__image-background wp-image-54"]').get_attribute(
            "src"))

        assert "California Real Estate" in driver.title
        print(driver.title)

        driver.find_element(By.ID, "send-us-a-message")
        driver.find_element(By.ID, "g2-name").send_keys("Zoryana")
        driver.find_element(By.ID, "g2-email").send_keys('zoryana_ukraine@yahoo.com')
        driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys('Hi, How May I Help You?')
        driver.find_element(By.XPATH, '//*[@class="pushbutton-wide"]').click()
        delay()

        try:
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "link")))
            print(" 'go back' link is VISIBLE")
        except TimeoutException:
            print("'go back' link is not VISIBLE")

        driver.find_element(By.CLASS_NAME, "link").click()
        print(driver.find_element(By.CLASS_NAME, "pushbutton-wide").get_attribute('type'))

    def tearDown(self):
        self.driver.quit()



class EdgeSearch(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()


    def test_search(self):
            driver = self.driver
            driver.get("https://qasvus.wordpress.com")

            def delay():
                time.sleep(random.randint(1, 3))

            driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()
            print(driver.find_element(By.XPATH,
                                      '//*[@class="site-title"]//*[text()="California Real Estate"]').get_attribute(
                "href"))
            print(driver.find_element(By.XPATH,
                                      '//*[@class="wp-block-cover__image-background wp-image-54"]').get_attribute(
                "src"))

            assert "California Real Estate" in driver.title
            print(driver.title)

            driver.find_element(By.ID, "send-us-a-message")
            driver.find_element(By.ID, "g2-name").send_keys("Zoryana")
            driver.find_element(By.ID, "g2-email").send_keys('zoryana_ukraine@yahoo.com')
            driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys('Hi, How May I Help You?')
            driver.find_element(By.XPATH, '//*[@class="pushbutton-wide"]').click()
            delay()

            try:
                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "link")))
                print(" 'go back' link is VISIBLE")
            except TimeoutException:
                print("'go back' link is not VISIBLE")

            driver.find_element(By.CLASS_NAME, "link").click()
            print(driver.find_element(By.CLASS_NAME, "pushbutton-wide").get_attribute('type'))

    def test_search_chrome_1120x550(self):
        driver = self.driver
        driver.set_window_size(1120, 550)
        driver.get("https://qasvus.wordpress.com")

        def delay():
            time.sleep(random.randint(1, 3))

        driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()
        print(driver.find_element(By.XPATH,
                                  '//*[@class="site-title"]//*[text()="California Real Estate"]').get_attribute(
            "href"))
        print(driver.find_element(By.XPATH,
                                  '//*[@class="wp-block-cover__image-background wp-image-54"]').get_attribute(
            "src"))

        assert "California Real Estate" in driver.title
        print(driver.title)

        driver.find_element(By.ID, "send-us-a-message")
        driver.find_element(By.ID, "g2-name").send_keys("Zoryana")
        driver.find_element(By.ID, "g2-email").send_keys('zoryana_ukraine@yahoo.com')
        driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys('Hi, How May I Help You?')
        driver.find_element(By.XPATH, '//*[@class="pushbutton-wide"]').click()
        delay()

        try:
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "link")))
            print(" 'go back' link is VISIBLE")
        except TimeoutException:
            print("'go back' link is not VISIBLE")

        driver.find_element(By.CLASS_NAME, "link").click()
        print(driver.find_element(By.CLASS_NAME, "pushbutton-wide").get_attribute('type'))

    def tearDown(self):
        self.driver.quit()
