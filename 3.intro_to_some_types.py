# COMMENTS
# Comments in Python start with the hashtag character. They acan start at the beginning of a line like here.
print ("Inline Comment!") #Or can follow a line of code like here. In this case they are called an Inline comment.
# Multiline comments also exist and are created using triple quotes
'''
This here is an example.
Of a multiline comment!!
'''
# Comments however cannot appear in the middle of a string literal as a hashtag is simply treated as a hash character in a string and not as a comment creation character
print("The # character here does not create a comment")

# NUMBERS
# The Python charactercan act as a simple character of sorts and typing in an expression results in it producing the output
# This can be seen as an example in interactive mode
# Creating arithmetic expressions is easy in Python: we use +, /, -, * characters for arithmetic operations (they are called arithmetic operators) and the parentheses () for grouping
# There are two types of numbers that we will primarily be using: The integer numbers are of type int, and the decimal numbers ( Those with a fractional part) are type float
# Besides the standard four arithmetic operations, // operator is used for floor division (this is where you want an integer result for the division)
# % or modulo operator is used to return the remainder upon division of two numbers
# We can use the ** operator for powers E.g 2**4 is a pythonic way of saying 2 raised to the power 4

# INTRO TO VARIABLES
# The = operator, often called the assignment operator is used to assign a value to a variable
# Python is a DYNAMICALLY TYPED LANGUAGE which means you don't have to declare types alongside variables
# A dynamically tped language is one where types are determined at runtime not in advance
# If a variable is not previously defined it will return an error
# NOTE: In interactive mode, the last printed statement is stored in the _ variable

# Some Examples
a= 7
b= 4.5
added= a + b # When an operator has to deal with two different types of operands of int and float, it will convert all operands of type int to type float
result= ((3 + 7)/5 *3 ) % 3 -2
print(a)
print(b)
print(added)
print(result // a)

# Python supports multiassignment. The below examples are all valid and kind of unique to python

a, b= 1, 2
a=b=c=3


