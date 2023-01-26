import os
import time
from threading import Thread

from ZoryanaPleskun.BrowserStack import My_key
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or My_key.BROWSERSTACK_USERNAME
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or My_key.BROWSERSTACK_ACCESS_KEY
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"
BUILD_NAME = "browserstack-build-1"
capabilities = [
    {
        "browserName": "chrome",
        "browserVersion": "103.0",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "BStack Python sample",  # test name
        "buildName": BUILD_NAME,  # Your tests will be organized within this build
    },
    {
        "browserName": "firefox",
        "browserVersion": "102.0",
        "os": "Windows",
        "osVersion": "10",
        "sessionName": "BStack Python sample parallel-Firefox-Win10",
        "buildName": BUILD_NAME,
    },
    {

        "browserVersion": "14.1",
        "os": "OS X",
        "osVersion": "Big Sur",
        "sessionName": "BStack Python sample parallel-Safari-BigSur",
        "buildName": BUILD_NAME,
    },
]


def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())


def run_session(cap):
    bstack_options = {
        "osVersion": cap["osVersion"],
        "buildName": cap["buildName"],
        "sessionName": cap["sessionName"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    if "os" in cap:
        bstack_options["os"] = cap["os"]
    options = get_browser_option(cap["browserName"].lower())
    if "browserVersion" in cap:
        options.browser_version = cap["browserVersion"]
    options.set_capability('bstack:options', bstack_options)
    driver = webdriver.Remote(
        command_executor=URL,
        options=options)
    try:
        # test1 Chrome
        driver.get("https://qasvus.wordpress.com")

        # Maximize browser window
        driver.maximize_window()

        # Print link(href) for header message "California Real Estate"
        print(driver.find_element(By.XPATH, '//*[@class="site-title"]//*[text()="California Real Estate"]')
              .get_attribute("href"))

        # Print link(src) for first home image under "About us"
        print(driver.find_element(By.XPATH, '//*[@class="wp-image-55 size-full"]').get_attribute("src"))

        # Verify (do assert) "California Real Estate" in website title
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title

        # Print website title
        print(driver.title)

        #  Find "Send Us a Message" and verify it's present on the web page
        driver.find_element(By.ID, 'send-us-a-message')

        # Fill out and send the message form using one of the following tags:XPath, ID, Name, ClassName,
        # Link_Text or Link_Partial_Text
        driver.find_element(By.ID, 'g2-name').send_keys("Zoryana")
        driver.find_element(By.ID, 'g2-email').send_keys("zoryana_ukraine@yahoo.com")
        driver.find_element(By.ID, 'contact-form-comment-g2-message').send_keys("Hi, How may I help you?")
        driver.find_element(By.XPATH, '//*[@type = "submit"]').send_keys('\n')

        # Find "go back" button (link) and using one of the tags above click it to go back to the Main page.
        driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").send_keys('\n')
        time.sleep(2)

        # Once you'll get the Main page, verify it by finding and print "type" for "Submit" button
        print(driver.find_element(By.XPATH, '//*[@class="pushbutton-wide"]').get_attribute("type"))

        # method is used when you want to terminate the webdriver instance window
        driver.quit()

    except WebDriverException:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'elements failed to load"}}')
    except Exception:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'exception occurred"}}')
    # Stop the driver
    driver.quit()


for cap in capabilities:
    Thread(target=run_session, args=(cap,)).start()
