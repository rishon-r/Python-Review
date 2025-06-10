# LISTS

# Lists serve as our first encounter with COMPOUND DATA TYPES
# These are datatypes used to group together other values
# Lists are mutable which means their values can be changed in place
# Lists consist of comma separated values stored between square braces
# They can store multiple different kind of datatypes (values stored can be of any type)
# In a manner similar to strings, they can be indexed and sliced (this serves for all sequence data types)

li= [3.14, 'Apple', [1,2]] # It is possible to nest lists inside lists
# We can then access them via double indexes
print(li[2][0]) # Will print 1
print(li[0]) # prints 3.14
print(li[1:3]) # prints [ 'Apple', [1,2]]
# All slice operations create a new list containing the requested elements
li[1]= "Orange" # Changes li to [3.14, "Orange", [1,2]] (This shows mutability)
print(li)

# You can add new items to the end of the list using the append method
li.append(420) # adds 420 to the end of list
print(li)
# The built-in len() function also applies to lists and will return the number of elements in a given list

# IMPORTANT NOTE
# Simple assignment in Python never copies data
# Example:
new_li= li # Here, new li simply points to the same list that li refers to
# So changing li in any form will cause the changes to be reflected in new_li
# Example:
li[0]= 33
print(new_li[0]) # This will also print 33

# It is possible to assign to a slice. This often results in a change in the size of the list or clearing of the list entirely
# Examples:

li[1:2]=["A", "B", "C"]
print(li) # prints [33, "A", "B", "C", [1,2], 420]
li[:]=[] # Will make li point to an empty list

# MEMBERSHIP OPERATORS: in, not in are the two membership operators that are used to check whether or not a particular value belongs in a sequence.
# They return a boolean value as result

# LIST METHODS
# There are a series of useful methods that can be used on lists
li=[1,2,3,4,5]
print(li)
# 1. list.append() is used to add a ssingle element to the back of the list
li.append(6)
print(li)

# 2. list.extend() allows you to add multiple elements to the back of a list.
# It take one argument which is a sequence and every individual element of the sequence is added as an individual element to the list
li.extend('hello')
print(li)
li.extend([[7,8,9]])
print(li)
# Appending a sequence to the list results in the entire sequence being added as a single element to the list

# 3. list.pop() removes and returns last element of the list if no argument is provided. 
# It takes an optional argument which is an index and removes the element at index mentioned if specified instead of arbitrarily removing last element
# It returns an IndexError if an invalid index is provided

li.pop()
print(li)
li.pop(3)
print(li)

# 4. list.remove() takes an element as an argument and removes the first occurence of that element from the list
# Returns ValueError if the element is not found
li.remove('l')
print(li)

# 5. list.index() takes an element that is a part of the list as an argument and returns the index of its first occurence
# If the element does not exist, it returns ValueError
print(li.index('h'))

# 6. list.clear() removes every eelement in the list without deleting the list object. The list just becomes an empty list
li.clear()
print(li)

li=[1,2,3,4,5]
print(li)

#7. list.reverse() reverse the order of elements in the list in place
li.reverse()
print(li)

# 8. list.sort() sorts the list in place, it takes an optional keyworrd argument called reverse which can be Boolean value either true or false. 
# It is False by default. If True it will sort in descending order
# This is done provided that all elements in the list are of a comparable type

li.sort()
print(li)
li.sort(reverse=True)
print(li)

# 9. list.insert(pos, elem): Inserts the element elem at the index mentioned as pos.
#  All the elements in list at that index and further will be moved one index up

li.insert(3, 300)
print(li)

# 10. li.count(elem) counts the number of times an element elem occurs in the list. Returns 0 if the element is not found
print(li.count(1))

# 11. list.copy() creates a shallow copy of the list
new_li=li.copy()
print(li, new_li)
li.append(5)
print(new_li) # changes made in li are reflected in new_li as it is a shallow copy

# Note that insert, remove and sort all return no value (i.e they return None)
# This is a design principle implemented through all mutable objects in Python

# del statement
# The del statement provides a way of deleting elements from a list using indexes and slices rather than using their value unlike remove
# It differs from pop() as it does not return a value
# Examples:

del li[1] # deletes element at index 1

del li[3:] # deletes every element from list after and including index position 3

del li # clears the list and deletes the list object

# USING LISTS AS STACKS
# With the help of list methods, a list in Python can very easily function as a Stack which is a LIFO (Last in, First out) daa structure
# Simply use list.append() to add an element to the back of the list (top of stack) and list.pop() without index mentioned as an argument to return the element last added to list with append.
# Example:
li= [7,6,4,3,2]
li.append(6) # adding to top
li.pop() # removes element at the top

# USING LISTS AS QUEUES
# A Queue is a FIFO data structure (First in, First out)
# Although it is possible to use a list as a queue, lists don't provide an efficient implementation of a queue
# This is because while appends and pops from the end of the list are fast, insert and pop with index operations which are required for queues are slow
# This is because an insert or pop with index operation involves reshuffling of all other elements in the list and this is slow
# collections.deque provides a much better implementation with fast appends and pops from both ends
# An example from the documentation:

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

print(queue)                      # Remaining queue in order of arrival





