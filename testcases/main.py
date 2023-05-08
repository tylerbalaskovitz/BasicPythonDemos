import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    #used at the beginning to begin running test cases.
    def setUp(self):
        print("setup test")
        self.driver = webdriver.Chrome("/home/tyler/Documents/WebDriver/chromedriver")
        self.driver.get("http://www.python.org")

    #If you have test_NameOfTheTest, the unittest module detects these as tests and automatically executes the tests
    def test_example(self):
        print("Test")
        assert False

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