import unittest

class SearchEnginesTest(unittest.TestCase):

    def test_google(self):
        list = {"python", "java", "ruby"}
        #self.assertIn("python", list)
        self.assertNotIn("php", list)

if __name__ == '__main__':
    unittest.main()
