from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#path of the chrome webdriver used to open a web browser
PATH = "/home/tyler/Documents/WebDriver/chromedriver"

#First thing to always do is determine the driver of and the corresponding browser.
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net")

#finds the text that shows up as a link and access the element from that. IE if it's a text then it has a link to it, and the link's text is Python Programming
link = driver.find_element(By.LINK_TEXT, "Python Programming")
link.click()

try:
    #waits for the webdriver to find something for up to 10 seconds. The second parameter of the function. If it's more than 10 seconds, then things will time out
    #the program will crash from there. 
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    #used to clear a textbox. 
    #element.clear()
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

    driver.back()
    driver.back()
    driver.back()
    driver.forward()
    driver.forward()
    
except:
    driver.quit()

#sometimes a page will load in a weird way. So, you have to make sure the elements are loaded before firing something off. 