#!/usr/bin/env python
"""
@author [mst]
@file helloworld.py
@brief basic python constructs adn syntax

log/gains:
-lynda.com 'Learning Python' course examples
-basic classes and function calls, local/global arguments
-variable arguments
-dates and times, timedeltas
-formatting as strings and performing calculations


 @version 0.1 2021
"""



# [demo] classes and inheritance
class myClass():
    def method1(self):
        print ("myClass method1")

    def method2(self, someString):
        print ("myClass method2: " + someString)

class anotherClass(myClass): # [mst] inherited
    def method2(self):
        print ("anotherClass method2")

    def method1(self):
        myClass.method1(self)
        print ("anotherClass method1")


# [demo] define a function
def func1():
    print ("I am a function")

# function with default value for an argument (x is optional)
# [demo] there is no for-each loop in python
# [demo] the '_' directs an unused variable (we could put an un-used i here)
def power(num, x=1):
    result = 1; # this will handle the power of 0
    for _ in range(x):
        result = result * num
    return result

# function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

def inputs():
    # [demo] basic STDIN input readout, protected by a simple try block
    try:
        n = int(input())

        # [demo]  range boudaries definitions
        for i in range(1,n+1):
            print(i, end='')
        print("\n")
    except:
        print("Couldn't resolve an number")

def arrays():
    # [demo] a proper way to init a 2d array (can be used via nested loops)
    # a simple 'memo = [[0]*n]*m' would lint row arrays and cause wrong behavior
    # source: https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
    rows, cols = 3,4
    memo = [[1 for i in range(cols)] for j in range(rows)]
    print(f"array {memo=}")

def scopes():
    f = "abc"   # scope testing variable
    someFunction()
    print (f"{f=}")

def func_and_classes():
    # functions and return values
    func1()
    print (func1())
    print (func1)   #[mst] will return None since no return value
    print (f'power(2, 3) = {power(x=3, num=2):_>8}') # explicit parameter targeting (this is an f-string with padding configuration)

    c = myClass()
    c.method1()
    c.method2("This is a string")
    c2 = anotherClass()
    c2.method1()
    c2.method2()





################## DRIVER
def main():
    print ("hello world!")

    # using the enumerate() function to get index: it will zip indexes and list values
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for i, d in enumerate(days):
        print (i+1, d, end=' ')
    print("")

    grade = 73
    min = 55
    max = 100
    if grade > min and grade < max: print ("passing grade")


    # multiple conditions can be compiled to a list
    conditions =[
        grade > min,
        grade < max
    ]
    if all(conditions): print ("passing grade")




    # basic aspects testing:

    # func_and_classes()
    # scopes()
    # arrays()
    # inputs()



# Global vs. local variables in functions
def someFunction():
    #global f #[mst] this would take the global f
    f = "def"
    print ("some funct: " + str(f))

# [mst][demo] this is a check for running via command line
# the __name__ parameter will hold the invoking method,
# which is set to __main__ when the app is run directly
if __name__ == ("__main__"):
    main()
