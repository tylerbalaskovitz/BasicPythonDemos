from selenium import webdriver

#gives access to using the keyboard for automation
from selenium.webdriver.common.keys import Keys
import time

PATH = "/home/tyler/Documents/WebDriver/chromedriver"

#First thing to always do is determine the driver of and the corresponding browser.
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net")

print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(3)

driver.quit()