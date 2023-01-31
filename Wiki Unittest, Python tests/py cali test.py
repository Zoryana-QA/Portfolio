from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Elements search via locators
from selenium.webdriver.common.by import By
import time

# Use Chrome browser
driver = webdriver.Chrome()
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
