# STRINGS
mystring = 'abcdefg'
print(mystring)
print(mystring[2:])

# Slicing
print(mystring[:3])
print(mystring[2:5])
print(mystring[::2]) # step size - grab every 2nd char in string

# Basic formatting
#x = mystring.upper()
x = mystring.capitalize()
my_split_str = 'Hello World'
print(my_split_str.split(' '))
print(x)

# Print Formatting
x = "Insert another string here: {}".format("INSERT ME")

print(x)
print("Item one: {x} Item two: {y}".format(x = "dog", y = "cat"))
