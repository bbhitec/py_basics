'''
 [mst] pytests.py
 demonstrating pytests
 based on entries in the enki app
 
 log:
 -2021.01: -initial draft
 
Created on Jan 29, 2021
@author: mst
'''

from multiply import mult

def test_one():
    # python has a more intelligent assertion handling than the unittest lib
    # this shoul be run with "pytest <module_name.py>"
    assert mult(3,3) == 9

def test_two():
    assert mult(g,2) == "gg"
    
