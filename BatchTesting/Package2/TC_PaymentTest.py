import unittest

class PaymentTest(unittest.TestCase):

    def test_PaymentInDollar(self):
        print("This is payment in dollar test.")
        self.assertTrue(True)

    def test_PaymentInTaka(self):
        print("This is payment in taka test.")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()