# TUPLES
# Tuples work similarly to lists except for two main key differences
# DIFFERENCE 1: Tuples use parentheses instead of square brackets []
# DIFFERENCE 2: Tuples are immutable objects whereas lists are mutable objects (Tuples are often called heterogenous sequences while lists are called homogenous sequences)
# This means values in a tuple cannot be changed in place

# In Python, objects like lists, tuples and strings are referred to as sequence data types
# Sequence data types are similar in ways of indexing and slicing
# Example:

t= (1,2, "hello", [1,2,3])
print(t[0])
print(t[1:3])

# As tuples are immutable, you can't assign a new value based on position. e.g t[0]= 4 would result in an error

# Although tuples are immutable, they may contain mutable objects as elements and one is allowed to change values of this mutable object in place.
print(t)
t[3][1]="changed"
print(t)

# SINGLE ELEMENT TUPLES
# When creating single element tuples, it is important to place a comma of the element.
# Otherwise, the Python interpreter considers the object to be the same type as the element inside the single element tuple
# Example:
t=(3)
print(t, type(t)) # t here will be of type integer
t= (3,)
print(t, type(t))
# NOTE: The type() function is a built in Python function that returns type of any object in Python
# Empty tuples are created with an empty set of parentheses
# Example:

t=()
print(t, type(t))

# SEQUENCE CONSTRUCTORS
# Lists, Strings and Tuples have respective sequence constructors list(), str() and tuple() respectively.
# These are used to convert a given sequence into a list, tuple or string respectively
# Example:

s="hello"
l= [1,2,3,4,5]

new_l=list(s)
new_s= str(l)
new_t= tuple(l)

print(new_l, new_s, new_t)

# One can also create empty sequences with the sequence constructor. Just don't provide an argument

new_l=list()
new_s= str()
new_t= tuple()

print(new_l, new_s, new_t)

# PACKING AND UNPACKING TUPLES
# NOTE: Tuples can also be created without mentioning parentheses

t= 3, 4, 5 # this is a valid way of creating the tuple (3,4,5)
# The above statement is a valid example of packing a tuple. The values 3, 4 and 5 are paked into the tuple
# The reverse operation is possible and called tuple unpacking

x, y, z= t
print(x, y, z)

# This is in general called sequence unpacking and can be applied to any sequence
# Example:
s= "hello"
var1, var2, var3, var4, var5, var6= s
print(var1, var2, var3, var4, var5, var6)

# Note that multiple assignment is really just a combination of tuple packing and sequence unpacking.
