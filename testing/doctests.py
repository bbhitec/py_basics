'''
 [mst] doctests.py
 demonstrating doctests
 based on entries in the enki app
 
 log:
 -2021.01: -initial draft

Created on Jan 29, 2021
@author: mst
'''

#from multiply import mult
import doctest

def multiply(a,b):
    # this is the syntax to define a doctest
    # this should be run via the shell as 'python <module_name>' and can be verbosed by adding '-v'
    """
    Test custom stuff:
    >>> multiply(3,3)
    9
    """
    return a * b

if __name__ == ("__main__"):
    doctest.testmod()   # this will enable doctests readout