#
# [mst] comprehensions_generators.py
# simple python comprehenshions and generators doodle
# - initial: comprehenshions, lamda functions
# - generator intro
# - some lists, sets, dictionaries nuances
#
#

########## list comprehensions ##########
nums = [1,2,3,4,5,6,7,8,9,10]

# simple: I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print (my_list)

print ([n for n in nums]) # can be equally written as a comprehension... (the "n for n" part)
print ([n*n for n in nums])	# operations within comprehensions
print (list(map(lambda n: n*n, nums))) # map (apply a function on a sequence) + lambda expression (less readable)
print ([n for n in nums if n%2 ==0]) # conditions in comprehensions
print (list(filter(lambda n: n%2 ==0, nums))) # filter + lambda will have the same effect

#pairs\tuples are welcome
pairs_list = []
for letter in 'abcd':
    for num in range(4):
        pairs_list.append((letter,num))
print (pairs_list)
print ([(a,b) for a in 'abcd' for b in range(4)]) # much easier and read-friendly as a comprehension


########## dictionary comprehensions ##########
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print (list(zip(names, heroes))) # [demo] zip will make tuples\pairs out of each two lists


hero_dict = {}	# init a dictionary
for name,hero in zip(names,heroes):
    hero_dict[name] = hero	# manually create a dictionary, key:name value:hero
print (hero_dict)
print (dict(zip(names, heroes))) # [demo] same effect as the loop above

print (dict({name: hero for name, hero in zip(names,heroes)})) # easier with a comprehension
print (dict({name: hero for name, hero in zip(names,heroes) if name!='Clark'})) # can use conditions


########## set comprehensions ##########
nums2 = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()	# [demo] a set is a list with no repetition
for n in nums2:
    my_set.add(n)
print (my_set)
print (set({n for n in nums2}))


########## generators ##########

# [demo] a simple generator is a function-object that runs real-time
# * not kept in memory. generates quickly but generally slower to work over
#   whereas lists are stored in memory and thus are generally faster to work with
# * (in py2: 'range' will make a list and store in memory)
def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)

for i in my_gen:
    print (i)

# a generator object is made to iterate through. it is not stored in the memory
x = (i for i in range(5))
print (x)   # this will print a pointer to a generator object
print (type(x))
[print (i) for i in x]    # print out the generated values

