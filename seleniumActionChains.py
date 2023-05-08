from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "/home/tyler/Documents/WebDriver/chromedriver"

#First thing to always do is determine the driver of and the corresponding browser.
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker")

driver.implicitly_wait(5)

cookie = driver.find_element("ID", "bigCookie")
cookie_count = driver.find_element("ID", "cookies")

items = [driver.find_element("ID", "productsPrice" + str(i)) for i in range (1, -1, -1)]


#creates a list of actions to be performed similar to a queue and is performed with the .perform() method on the actions
#you need the .perform() method to do the actions that are within the queue 
actions = ActionChains(driver)

actions.click(cookie)

for i in range(5000):
    actions.perform()

