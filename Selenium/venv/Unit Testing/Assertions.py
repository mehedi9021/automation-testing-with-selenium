import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):

    def test_google(self):
        self.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        pageTittle = self.driver.title
        #self.assertEqual("Google", pageTittle, "Title is not equal")
        #self.assertNotEqual("Google",pageTittle, "Title is equal")
        #self.assertTrue(pageTittle == "Google")
        self.assertFalse(pageTittle == "Google")


if __name__ == '__main__':
    unittest.main()