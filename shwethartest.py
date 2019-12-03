'''
Created on Dec 2, 2019

@author: shwethar
'''

import unittest
from geeksforgeeks.algorithm import isTriplet
class isTripletTest(unittest.TestCase):
    def test(self):
        array = [5, 1, 4, 6, 3] 
        ar_size = len(array) 
        self.assertEqual(isTriplet(array, ar_size), True)
        
        array1 = [1, 2, 3, 4, 5]
        ar_size = len(array1)  
        self.assertEqual(isTriplet(array1, ar_size), False)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
