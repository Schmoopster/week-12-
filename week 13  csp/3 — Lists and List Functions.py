
# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# Lists are part of the collections family in Python
# my_list = [1, 2, 3, 4, 5]
# print(my_list) # [1,2,3,4,5]
# print(len(my_list)) #5
# print(type(my_list)) #<class 'list'>
# print(my_list[0]) #1
# print(my_list[1:4]) # [2, 3, 4]
# print(my_list[1:])
# print(my_list[:-1]) # [1, 2, 3]
# # Reversing the list
# print(my_list[::-1]) # [5, 4, 3, 2, 1]
# # Modifying a list
# my_list.append(6) # adds 6 tp the end of the list
# print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8]
# my_list.extend([7,8])
# print(my_list)
# my_list.extend([9, 10, 11])
# print(my_list)
# # Remove the last item
# my_list.pop()
# print(my_list) # [1, 2, 3, 4, 5, 6, 7]
# # Sort the list in ascending order
# my_list.sort()
# print(my_list)
# my_list.reverse()
# print(my_list)
# # Remove a specific value
# my_list.remove(4)
# print(my_list)
# # add 50 more to the end of the list
# new_list = list(range(12, 120))
# print(new_list)
# my_list.append(new_list)
# print(my_list)
# print(my_list[ : : 3])
# print(my_list[ : : 10])
# del my_list[ : : 3]
# print(len(my_list))
# print(my_list)
#list frunctions
# .append() - adds an item to the end of the list
# .extend( - adds mutiple items to the end of the list
# .pop() - removes and returns an item at a given index
#   (default is the lastitem)
# .remove() - removes the first occurence of a specific value
# .sort() - sorts the list in ascending order 
# .reverse() reverses the order of the list
# why is a list more useful  than a variable?
# A list can hold multiple values, while a variable can only hold one value at a time
# cakes = ['chocolate', 'vanilla', 'red velvet', 'carrot']
# print(cakes)
# #access the first item
# print(cakes[0])
# #access the last item 
# print(cakes[-1])
# cakes[0] = 'strawberry'
# print(cakes)
# cakes[1] = 'chocolate'
# print(cakes)
# cakes.pop()
# print(cakes)
# cakes.insert(2, 'funfetti')
# print(cakes)

# Examples:

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.
fruit_list = ['orange', 'pineapple', 'apple', 'banana', 'blueberries']
# Print the second and last item.
print(fruit_list[1])
print(fruit_list[-1])
# Add a new item using .append().
fruit_list.append('cherry')
print(fruit_list)
# Remove the first item using .pop(0).
fruit_list.pop(0)
print(fruit_list)
# Reverse your list using .reverse().
fruit_list.reverse()
print(fruit_list)
# Create a list of 3 lists (matrix), and access the middle element.
#setes = {1,2,3,}
#setes are unordered collections of unique items
#setes fo not support slicing ot indexing
#sets are mutable meaning you can add or remove items
#sets are created using curly brackets
#sets don't alloq duplicate items
my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))
#remove an item from the list
my_set.remove(3)
print(my_set)
#chekc if an item is in the set
print(4 in my_set)
print(3 in my_set)

#tuples are ordered collections of lists 
#tuples are imutable meaning you cannot modify them after creation 
#tuples are creaed using pearenthesis 
my_tuple = (1,2,3,4,5)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[1:4])
#trying to modify the tuple will result in an error