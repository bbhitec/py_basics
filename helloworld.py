# [mst] helloworld.py 
# basic python constructs
# based on the lynda.com 'Learning Python' course
#
# log:
# -basic classes and function calls, local/global arguments
# -variable arguments
# -dates and times, timedeltas
# -formatting as strings and performing calculations
#



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

#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


def main():
    print ("hello world!")

    f = "abc"

    # using the enumerate() function to get index: it will zip indexes and list values
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for i, d in enumerate(days):
        print (i+1, d)
  
    # functions and return values    
    func1()
    print (func1())
    print (func1)   #[mst] will return None since no return value
    print (f'power(2, 3) = {power(x=3, num=2):_>8}') # explicit parameter targeting (this is an f-string with padding configuration)

    someFunction()
    print (f)
    
    c = myClass()
    c.method1()
    c.method2("This is a string")
    c2 = anotherClass()
    c2.method1()
    c2.method2()
    
    # basic STDIN input readout
    n = int(input())    
    
    # range boudaries definitions
    for i in range(1,n+1):
        print(i, end='')
    


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
