'''
Created on Sep 16, 2018
@author: rachelk4
'''
import unittest
from geeksforgeeks.algorithm import isTriplet
class isTripletTest(unittest.TestCase):
    def test(self):
        ar = [3, 1, 4, 6, 5] 
        ar_size = len(ar) 
        self.assertEqual(isTriplet(ar, ar_size), True)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
