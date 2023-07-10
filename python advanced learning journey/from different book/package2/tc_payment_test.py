import unittest
class paymentTest(unittest.TestCase):

    def test_payment_in_dollors(self):
        print("this is payment in dollors test")
        self.assertTrue(True)


    def test_payment_in_rupees(self):
        print("this is payment in rupees test")
        self.assertTrue(True)


if __name__  == '__main__':
    unittest.main()