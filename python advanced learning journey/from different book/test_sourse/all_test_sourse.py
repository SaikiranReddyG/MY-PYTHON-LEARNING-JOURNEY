import unittest
from package1.tc_logintest import loginTest
from package1.tc_signuptest import signupTest

from package2.tc_payment_test import paymentTest
from package2.tc_payment_returns_test import paymentretursTest

tc1 = unittest.defaultTestLoader().loadTestsFromTestcase(loginTest)
tc2 = unittest.load_tests().loadTestsFromTestcase(signupTest)
tc3 = unittest.load_tests().loadTestsFromTestcase(paymentTest)
tc4 = unittest.load_tests().loadTestsFromTestcase(paymentretursTest)

#creating testsuite

sanity_testsuite = unittest.testsuite()([tc1, tc2])    #this is a sanity test suite

unittest.TextTestRunner().run(sanity_testsuite)