'''
 [mst] unit_tests.py title
 playing around with unit testing lib in python
 based on entries in the enki app
 
 [demo] to run the built-in unit tests:
 -A: import the unittest lib
 -B: derive a class from unittest.TestCase
 -C: define test methods named 'test_<testname>'
 -D: have unittest.main() in my class

 log:
 -2021.01: -initial

Created on Jan 29, 2021
@author: mst
'''

import unittest # A: import the unittest lib

class simple1(unittest.TestLoader): # B: derive a class from unittest.TestCase
    
    def test_True(self):    # C: define test methods named 'test_<testname>'
        self.assertTrue(True)
    def test_Upper(self):
        self.assertEqual(
            'enki'.upper(),
            'ENKI'
            )        

################## DRIVER
def main():
    print ("[mst] unit tests doodle")
   
if __name__ == ("__main__"):
    unittest.main()     # D: have unittest.main() in my class
                        # this will allow us to run the unit tests
    main()