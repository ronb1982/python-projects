# Lists
# mylist = [1,2,3]
mylist = ['stringstuff', 1,2,3,23.2,True, [1,2,3]]
print(mylist)
print(len(mylist))

mylist = ['a', 'b', 'c']
print(mylist[0])
print(mylist[1:])
print(mylist[:3])

# mylist[0] = 'NEW ITEM'
# print(mylist)

# append new item to list
mylist.append('NEW ITEM')
print(mylist)

numbers_array = ['1', '2', '3']

# append list to a list
mylist.append(numbers_array)
print("Appending list: {}".format(mylist))

# remove item from the end of list
mylist.remove(numbers_array)
print("New list after removal: {}".format(mylist))

# extend the current list by adding a new list
mylist.extend(numbers_array)
print("Extending list: {}".format(mylist))

# reverse list
mylist.reverse()
print(mylist)

# sort list
mylist.sort()
print(mylist)

# index a nested list
mylist = [1,2,['x', 'y', 'z']]
print(mylist[2])
print(mylist[2][1]) # return an item within the nested list


# LIST COMPREHENSION - grab the first column in each row of the matrix array
matrix = [[1,2,3], [4,5,6], [7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)
