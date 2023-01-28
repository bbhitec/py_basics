#!/usr/bin/env python
"""
@author [mst]
@file lists_tuples_dict.py
@brief basic python constructs: lists vs tuples, dictionaries

log/gains:
-hashmap/dict
-list and tuples basics
-2021.01: -initial

@version 0.1 2021
"""

# demonstrating lists and tuples stuff
def list_vs_tuples():

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

    # [demo] since set can only have unique members, we can use it to remove duplicates
    ar = [1,2,2,3,4]
    ar_no_duplicates = list(set(ar))
    print(f"{ar_no_duplicates=}")



# demonstrating python dictionatries/hash map
def topKFrequent():#(words: [str], k: int) -> [str]:

    words=["i","love","leetcode","i","love","coding"]
    k=3
    print(f"{words=} {k=}")


    dictionary = {}
    res = []

    # [demo] built in 'sort' can sort strings lexicographically
    words.sort()

    for word in words:
        if word in dictionary: dictionary[word] = dictionary[word] + 1
        else: dictionary[word] = 1

    # [demo] sorting dict by values: results in a list of tuples
    sorted_dict = {key: val for key, val in sorted(dictionary.items(), key=lambda x:x[1], reverse=True)}

    # build a list out of first k keys of a dictionary
    res = list(sorted_dict)[0:k]

    print (f"{res=}")
    # return res


################## DRIVER
def main():

    list_vs_tuples()
    # topKFrequent()


if __name__ == "__main__":
    main()