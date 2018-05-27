# # x = 25
# # 
# # def my_func():
# #     x = 50
# #     return x
# # 
# # print(x)
# # print(my_func())
# # print(x)
# 
# # LOCAL
# result = lambda x: x*2
# print(result('35'))
# 
# # Enclosing function locals
# name = 'This is a global name'
# 
# def greet():
#     #name = "sammy"
#     def hello():
#         print("hello " + name);
# 
#     hello()
# 
# greet()
# 
# x = 50
# 
# def func():
#     global x # can be used to reference global variables
#     x = 1000
# 
# print("before function call, x is: ", x)
# func()
# print("after function call, x is: ", x)
#=================================================================================
# Object-oriented programming
# CLASSES
# class Dog():
#     # class object attributes
#     species = "mammal"
# 
#     # Constructor - special method - must pass in self
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name
# 
# mydog = Dog('Lab', 'Sammy')
# print(mydog.breed)
# print(mydog.name)
# print(mydog.species)
# 
# class Circle():
#     pi = 3.14
# 
#     def __init__(self, radius = 1):
#         self.radius = radius
# 
#     def area(self):
#         return self.radius * self.radius * Circle.pi
# 
#     def set_radius(self, new_r):
#         self.radius = new_r
# 
# myc = Circle(3)
# myc.set_radius(999)
# print(myc.area())

# INHERITANCE
# class Animal():
# 
#     def __init__(self):
#         print("ANIMAL CREATED")
# 
#     def whoAmI(self):
#         print("ANIMAL")
# 
#     def eat(self):
#         print("EATING")
# 
# # Pass in base class to Dog constructor
# class Dog(Animal):
# 
#     def __init__(self):
#         print("DOG CREATED")
# 
#     def bark(self):
#         print("WOOF!")
# 
# mydog = Dog()
# mydog.whoAmI()
# mydog.eat()
# mydog.bark()

# SPECIAL METHODS
# class Book():
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
# 
#     # Special method that returns actual string representation of this object
#     def __str__(self):
#         return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)
# 
#     def __len__(self):
#         return self.pages
# 
#     def __del__(self):
#         print("the book is destroyed!")
# 
# b = Book("Python", "Ron", 200)
# print(b)
# 
# print(len(b))
# del bytes

# ERRORS AND EXCEPTIONS
# try:
#     f = open('simple.txt', 'r') # open() opens file. Specify 'r' (read-only) or 'w' (write access)
#     f.write('Test write to simple text!')
# except:
#     print('ERROR: COULD NOT FIND FILE OR READ DATA!')
# else:
#     print('SUCCESS!')
#     f.close()
# finally:
#     print('I ALWAYS WORK NO MATTER WHAT!')

# REGULAR EXPRESSIONS (REGEX)
import re
# patterns = ['term1', 'term2']
# 
# text = 'This is a string with term1, but not the other!'
# match = re.search('term1', text)
# print(int(match.start()))
# 
# split_term = '@'
# email = 'user@gmail.com'
# print(re.split(split_term, email))

# for pattern in patterns:
#     print("I'm searching for: " + pattern)
#     if re.search(pattern, text):
#         print('MATCH!')
#     else:
#         print('NO MATCH!')

# find all instances of string
# print(len(re.findall('match', 'test phrase match in match middle')))
# 
# def multi_re_find(patterns, phrase):
#     for pat in patterns:
#         print('Searching for pattern {}'.format(pat))
#         print(re.findall(pat, phrase))
#         print('\n')
# 
# test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'
# test_patterns = ['sd*'] # Find s followed by 0 or more d's
# multi_re_find(test_patterns, test_phrase)
# 
# test_patterns = ['sd+'] # Find s followed by 1 or more d's
# multi_re_find(test_patterns, test_phrase)
# 
# test_patterns = ['sd?'] # Find s followed by 0 or 1 d's
# multi_re_find(test_patterns, test_phrase)
# 
# test_patterns = ['sd{3}'] # Find s followed by 3 d's
# multi_re_find(test_patterns, test_phrase)
# 
# test_patterns = ['sd{1,3}'] # Find s followed by 1 or 3 d's
# multi_re_find(test_patterns, test_phrase)
# 
# test_patterns = ['s[sd]+'] # Find s followed by 1 or more s's OR 1 or more d's
# multi_re_find(test_patterns, test_phrase)
# 
# test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
# test_patterns = ['[^!.?]+'] # Exclude (^) 1 or more instance of characters specified in brackets [] 
# multi_re_find(test_patterns, test_phrase)
# 
# test_patterns = ['[a-z]+'] # Find 1 or more instances within a-z (lowercase)
# multi_re_find(test_patterns, test_phrase)
# 
# test_patterns = ['[A-Z]+'] # Find 1 or more instances within a-z (uppercase)
# multi_re_find(test_patterns, test_phrase)
# 
# # Regex with escape characters
# test_phrase = 'This is a string with numbers 12312 and a symbol #hashtag'
# test_patterns = [r'\d+'] # Find 1 or more digits in string
# multi_re_find(test_patterns, test_phrase)
# 
# test_patterns = [r'\D+'] # Exclude numerical digits in string
# multi_re_find(test_patterns, test_phrase)
# 
# test_patterns = [r'\s+'] # Find whitespaces in string
# multi_re_find(test_patterns, test_phrase)
# 
# test_patterns = [r'\S+'] # Find non-whitespaces in string
# multi_re_find(test_patterns, test_phrase)
# 
# test_patterns = [r'\w+'] # Find alphanumeric characters in string
# multi_re_find(test_patterns, test_phrase)
# 
# test_patterns = [r'\W+'] # Find non-alphanumeric characters in string (special characters)
# multi_re_find(test_patterns, test_phrase)

# DECORATORS
# s = "GLOBAL VARIABLE"
# 
# def func():
#     mylocal = 10
#     print(locals())
#     print(globals()['s'])
# 
# func()
# 
# def hello(name = "Ron"):
#     return "Hello " + name
# 
# print(hello())
# mynewgreet = hello
# print(mynewgreet())
# 
# def hello(name = "Ron"):
#     print("THE HELLO() FUNCTION HAS BEEN RUN!")
#     def greet():
#         return "THIS STRING IS INSIDE GREET()"
#     def welcome():
#         return "THIS STRING IS INSIDE WELCOME!"
#     if name == "Ron":
#         return greet
#     else:
#         return welcome
# 
#     # print(greet())
#     # print(welcome())
#     # print("End of hello()")
# 
# x = hello()
# print(x())
# 
# def hello():
#     return "Hi RON"
# 
# def other(func):
#     print("HELLO")
#     print(func())
# 
# other(hello)
# 
# def new_decorator(func):
#     def wrap_func():
#         print("CODE HERE BEFORE EXECUTING FUNC")
#         func()
#         print("FUNC() HAS BEEN CALLED")
#     return wrap_func
# 
# # Decorator annotation that passes annotated method into the method specified in the annotation tag
# @new_decorator
# def func_needs_decorator():
#     print("THIS FUNCTION IS IN NEED OF A DECORATOR")
# 
# # Via reassignment    
# # func_needs_decorator = new_decorator(func_needs_decorator)
# # func_needs_decorator()
# 
# func_needs_decorator()

