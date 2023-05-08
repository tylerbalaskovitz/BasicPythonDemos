#Locator is used for keeping all the locators/selectors together in one place. 
from selenium.webdriver.common.by import By

#creating classes for objects that we want to find
class MainPageLocators(object):
    GO_BUTTON = (By.ID, "submit")

#put the locators for what you want to find in the search results page. 
class SearchResultsPageLocators(object):
    pass