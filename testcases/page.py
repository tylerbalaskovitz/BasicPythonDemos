#More of the selenium code is in page
#This is going to be the base class for all of the pages. 
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver