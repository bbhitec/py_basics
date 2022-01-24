# [mst] lists_tuples.py
# basic python constructs: lists vs tuples
#
# log:
# - 2021.01: - initial
# - list and tuples basics


def main():
    
    # a list:
    # -homogeneous collections, similar to what you'd use arrays for
    # -mutable, more functionality

    list_num = [1,2,3,4]    
       
    # a tuple:
    # -heterogeneous collections, similar to what you'd use 'structs' for in C
    # -fixed in size, immutable (can't append/extend/pop)
    # -can be used as a hash (since not mutable)
    tup_num = (1,2,3,4)  
    
    
    print(list_num)
    print(tup_num)
    
    # list of tuples
    list_23 = [('Swordfish', 'Dominic Sena', 2001), ('Snowden', ' Oliver Stone', 2016), ('Taxi Driver', 'Martin Scorsese', 1976)]
    print (list_23)
    
    # tuples can be used as dictionary keys since their immutability. lists cannot!
    key_val= {('alpha','bravo'):123} 
    print (key_val)
    
    
if __name__ == "__main__":
    main();