import unittest

def setUpModule(): #will execute before all class and all method present
    print("SetUpModule")

def tearDownModule(): #will execute before all class and all method present
    print("tearDownModule")

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self): #execute before all the test methods
        print("This is login test")

    @classmethod
    def tearDown(self): #execute after all the test method
        print("This is logout test")

    @classmethod
    def setUpClass(cls): #will execute when the class started
        print("Open application")

    @classmethod
    def tearDownClass(cls): #will execute at ending the class
        print("Close application")

    def test_search(self):
        print("This is search test.")

    def test_AdvanceSearch(self):
        print("This is advance search test.")

    def test_PrepaidRecharge(self):
        print("This is prepaid recharge test")

    def test_PostpaidRecharge(self):
        print("This is postpaid recharge test")


if __name__ == '__main__':
    unittest.main()