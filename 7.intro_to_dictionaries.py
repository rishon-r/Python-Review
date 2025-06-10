# DICTIONARIES

# Another very useful data type in Python is the dictionary
# They are often referred to as associative arrays in other language
# Dictionaries are defined as unordered collections of key: value pairs that are separated by commas and enclosed in curly braces {}
# Unlike sequences which are indexed by numbers, Dictionaries are indexed by keys
# Mentioning dictionary name followed by key name in this square brackets results in you referring to the value in the dictionary stored with that particular key
# You can access the value stored at key by typing: d[key]
# Keys in a dictionary must be of an immutable type while values can be of any type
# Tuples can be used as keys if the tuple consists of only immutable values
# It is a requirement that keys in a dictionary must be UNIQUE 
# A pair of curly braces on its own creates an empty dictionary
# Example: Working with a dictionary

d={} # creates empty dictionary
print(d)
new_d={1: "hello", 'A': 2}
new_d['A']= 'world' # changes value at key 'A'
new_d[2]= "hey" # creates new key 2 in the dictionary with value "hey"
print(new_d)
newer_d=dict() # creates a new empty dictionary using the dictionary constructor
#You can create a dictionary easily using the dict() function and keyword arguments
#Example:
example= dict(name="Jim", age=33, office="Dunder Mifflin")
print(example)

# Looping through a dictionary: Iterating through a dictionary iterates through the set of keys in the dictionary not the values
# The values however can be accessed easily if the keys and name of dictionary are known

for key in new_d:
    print(f"Key: {key} and Value: {new_d[key]}")

# Using any of the sequence constructor methods alongside a dictionary will create a sequence with only the keys in the dictionary
l= list(new_d)
print(l)

# 3 very useful dictionary functions

keys= new_d.keys() # This will return a ssequence consisting of only the keys in the dictionary
vals= new_d.values() # This will create a sequence consisting of only the values in the dictionary
its= new_d.items() # This will return a sequence consisting of all the key value pairs in dictionary stored as individual (key, value) tuples
print(keys)
print(vals)
print(its)

# DICTIONARY COMPREHENSIONS exist and can be used according to following syntax

d= {x: x**2 for x in range(10)}
print(d)

