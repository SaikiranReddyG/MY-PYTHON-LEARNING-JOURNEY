import unittest

class signupTest(unittest.TestCase):
    def test_signup_by_email(self):
        print("this is signup by email test")
        self.assertTrue(True)



    def test_signup_by_facebook(self):
        print("this is signup by facebook test")
        self.assertTrue(True)

    def test_signup_by_twitter(self):
        print("this is signup by twitter test")
        self.assertTrue(True)


if __name__  == '__main__':
    unittest.main()