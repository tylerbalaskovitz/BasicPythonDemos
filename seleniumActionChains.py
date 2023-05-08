from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "/home/tyler/Documents/WebDriver/chromedriver"

#First thing to always do is determine the driver of and the corresponding browser.
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker")




driver.maximize_window()
driver.implicitly_wait(20)
time.sleep(10)

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range (1, -1, -1)]


#creates a list of actions to be performed similar to a queue and is performed with the .perform() method on the actions
#you need the .perform() method to do the actions that are within the queue 

for i in range(5000):
    actions = ActionChains(driver).click(cookie).perform()
    count = int(cookie_count.text.split(" ")[0])
    print(count)
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_action = ActionChains(driver)
            upgrade_action.move_to_element(item)
            upgrade_action.click()
            upgrade_action.perform()
