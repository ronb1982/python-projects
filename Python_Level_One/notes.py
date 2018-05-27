# # Dictionaries - do not retain order
# my_stuff = {"key1":"value",'key2':'value2', 'key3': {'123':[1,2,'grabMe']}}
# print(my_stuff['key1'])
# print(my_stuff['key2'])
# print(my_stuff['key3']['123'][2]) # get "grabMe" string from dictionary
#
# my_stuff = {'lunch': 'pizza', 'bfast': 'eggs'}
# my_stuff['lunch'] = 'burger'
# my_stuff['dinner'] = 'pasta'
# print(my_stuff['lunch'])
# print(my_stuff)
#
# # Booleans - True, False, 0, 1
#
# # Tuples - immutable sequences - cannot overwrite values in collection
# t = (1,2,3)
# print(t[0])
# t = ('a', True, 123)
# print(t)
#
# # Sets - unordered collections of unique elements
# x = set()
# x.add(1)
# x.add(2)
# print(x)
# x.add(4)
# x.add(0.1)
# print(x)
# x.add(2)
#
# converted = set([1,1,1,1,1,2,2,2,2,4,4,4,4])
# print(converted)
#
# # IF statements
# if 1 < 2:
#     print('First Block')
#     if 20 < 3:
#         print("True!")
#
# # IF ELSE statement
# if 1 > 2:
#     print('hello')
# elif 3 == 3:
#     print('elif ran!')
# else:
#     print('last')
#
# # Loops
# # For Loops
# seq = [1,2,3,4,5,6]
# for item in seq:
#     print(item)
# d = {'Sam': 1, 'Frank': 2, 'Dan': 3}
#
# for k in d:
#     print(k)
#     print(d[k])
# # Tuples
# mypairs = [(1,2), (3,4), (5,6)]
# # tuple unpacking
# for tup1, tup2 in mypairs:
#     print(tup2)
#     print(tup1)
# i = 1
# while i < 5:
#     print('i is {}'.format(i))
#     i = i + 1

# Range functions
# for item in range(4, 10, 2):
#     print(item)
#
# x = []
# for i in range(1,5):
#     x.append(i)
#
# print(x)
# # List comprehension
# out = [num**2 for num in x]
# print(out)
# def my_func(param1 = 'default'):
#     """
#     THIS IS THE DOCSTRING
#     """
#     print('my first python function! {}'.format(param1))
# 
# my_func()
# 
# def hello():
#     return 'hello'
# 
# result = hello()
# print(result)

def add_num(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1 + num2
    else:
        return "Sorry, I need integers!"

result = add_num(2,3)
print(result)

# Filter
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num % 2 == 0

# filter() returns a new iterable list with the items in the passed-in sequence that returns true
evens = filter(even_bool, mylist)
print(list(evens))

# Lambda expression - just like anonymous functions - used to avoid defining new functions
new_evens = filter(lambda num: num % 2 == 0, mylist)
print("New evens list: {}".format(list(new_evens)))

# String methods
tweet = 'Go Sports! #Sports'
result = tweet.split('#')[1]
print(result)

# in keyword checks if collect contains element
print('x' in [1,2,3, 'x'])
    