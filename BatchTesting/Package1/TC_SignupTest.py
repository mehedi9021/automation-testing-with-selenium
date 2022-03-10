import unittest

class SignupTest(unittest.TestCase):

    def test_SignupByEmail(self):
        print("This is signup by email test.")
        self.assertTrue(True)

    def test_SignupByFacebook(self):
        print("This is signup by facebook test.")
        self.assertTrue(True)

    def test_SignupByTwitter(self):
        print("This is signup by twitter test.")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()