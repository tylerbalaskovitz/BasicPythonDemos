from locator import *
#More of the selenium code is in page
#This is going to be the base class for all of the pages. 
#Each class within the page.py file represents a webpage that we're going to test. 
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

#this says to use the methods from BasePage since BasePage is being inherited into the MainPage class. 
#So, __init__(self, driver)... doesn't need to be defined because the constructor from BasePage already handles this. 
class MainPage(BasePage):
    def is_title_matches(self):
        return "Python" in self.driver.title
    
    def click_go_button(self):
        #the * before, allows you to unpack/separate it into separate entities
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultPage(BasePage):
    def is_results_found(self):
        return "No results found." not in self.driver.page_source
    
