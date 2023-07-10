#meathods that instantanious a smallportion of the code and verify its behaviour
#steps to do unit testing -arrange (isolation and instancing)  -act (input data) - assert (check the data)
#the "first principal"
#F  --  fast running
#I  --  indepemdent
#R  --  repeatable
#S  --  self validating
#T   --  timely
import unittest
#from power
#import power_num
class Testpower(unittest.TestCase):        #Test the function power_num from module power.py
    def Test_power_int(self):
        self.assertEqual(power_num(2,3), 8)

        def Test_power_float(self):
            self.assertEqual(power_num(1.5, 2),  2.25)



if __name__  == '__main__':
    unittest.main()