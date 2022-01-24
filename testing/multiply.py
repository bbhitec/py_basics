'''
 [mst] multiply.py
 this is a simple module to run test on

 log:
 -2021.01: -initial draft


Created on Jan 29, 2021
@author: mst
'''

def mult(a,b):
    """
    Test custom stuff:
    >>> mult(3,3)
    9
    """
    return a * b



# make this sort-of script-runnable
if __name__ == ("__main__"):
    import sys
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    if arg1.isnumeric:
        print(mult(int(arg1),arg2))
    else:
        print ("USAGE: arg1 must be a digit")
    