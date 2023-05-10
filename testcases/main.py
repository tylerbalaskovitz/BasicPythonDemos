import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    #used at the beginning to begin running test cases.
    def setUp(self):
        print("--setup test--")
        self.driver = webdriver.Chrome("/home/tyler/Documents/WebDriver/chromedriver")
        self.driver.get("http://www.python.org")

    #If you have test_NameOfTheTest, the unittest module detects these as tests and automatically executes the tests
    def test_example(self):
        print("Test")
        assert False

    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        #Comma says do the following operations afterwards
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    #Since this doesn't start with test_* it will not be executed with the class being tested
    def not_a_test(self):
        print("this won't print")    

    def test_example_2(self):
        assert True    

    #ran at the end to clean up tests. 
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()