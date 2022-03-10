import unittest

class AppTesting(unittest.TestCase):

    def test_search(self):
        print("This is search test.")

    @unittest.SkipTest #decorator
    def test_AdvanceSearch(self):
        print("This is advance search test")

    @unittest.skip("This testcase is not yet ready")
    def test_PrepaidRecharge(self):
        print("This is prepaid recharge test")

    @unittest.skipIf(1==1, "One is not equal one")
    def test_PostpaidRecharge(self):
        print("This is postpaid recharge test")

    def test_facebookLogin(self):
        print("This is facebook login test")

    def test_twitterLogin(self):
        print("This is twitter login test")

if __name__ == '__main__':
    unittest.main()