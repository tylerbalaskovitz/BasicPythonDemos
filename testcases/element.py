#this will represent one element on the page, like a search bar, etc.
from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):
#this is used for setting the value of an object. Essentially, this class is used for creating getters and setters within a class. 
    def __set__(self, obj, value):
            driver = obj.driver
            WebDriverWait(driver, 100).until(
                lambda driver: driver.find_element_by_name(self.locator))
            driver.find_element_by_name(self.locator).clear()
            driver.find_element_by_name(self.locator).send_keys(value)

        #no longer have to wait for that element, but use the BasePageElement class instead
    def __get__(self, obj, owner):
            driver = obj.driver
            WebDriverWait(driver, 100).until(
                lambda driver: driver.find_element_by_name(self.locator))
            element = driver.find_element_by_name(self.locator)
            return element.get_attribute("value")