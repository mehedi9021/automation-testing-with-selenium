import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):

    def test_google(self):
        #driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        driver = None
        self.assertIsNone(driver)
        #self.assertIsNotNone(driver)

if __name__ == '__main__':
    unittest.main()