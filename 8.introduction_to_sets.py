# SETS
# Python provides an implementation for the mathematical set
# It is basically an unordered collection with no duplicate elements
# Consists of values separated by commas and enclosed in curly braces {}
# Some common use cases of sets are eliminating duplicate entries and using membership operators for testing
# You can create a set using the set() function
# To create an empty set you cannot use {} but must instead use the set() function
# Using {} on its own will result in creation of an empty dictionary not an empty set
# Some examples:

s= {"hello", 1, 2, "bye", 2} #mentioning a duplicate 2 here will not result in an error but simply the 2 not getting stored the seconnd time
print(s)
s= set("abracadabra")
print(s) # You see that duplicate values of a and b are not stored in the set

# SET COMPREHENSIONS
# Similar to list comprehensions, set comprehensions are also supported by Python
# Example

s= {x for x in range(10)}
print(s)