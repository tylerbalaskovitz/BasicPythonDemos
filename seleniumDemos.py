from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#gives access to using the keyboard for automation

import time

PATH = "/home/tyler/Documents/WebDriver/chromedriver"

#First thing to always do is determine the driver of and the corresponding browser.
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net")

print(driver.title)

search = driver.find_element("name", "s")
search.send_keys("test" + Keys.RETURN)


try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements(By.TAG_NAME, "article")
    for article in articles:
        header = article.find_element(By.CLASS_NAME, "entry-summary")
        print(header.text)
finally:
    driver.quit()


#this allows you to scrape and access the entire website with driver.print_source
#print(driver.page_source)

#the older version of sleneium had a method for each element type, now you type the type of method, id, name, class etc. as the first parameter and then the name of
#the element in the second one. 
#main = driver.find_element("id", "main")
#print(main.text)

time.sleep(3)

driver.quit()