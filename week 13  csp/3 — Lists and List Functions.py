
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

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.