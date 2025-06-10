# LAMBDA FUNCTIONS
# A lambda expression or lambda function in Python refers to a small anonymous function
# A lambda expression does not need to be bound to a name, although it can be
# They can be used wherever a function object is required but are syntactically restricted to one line
# A lambda expression hence cannot use any statements such as if, for while, etc.
# The lambda expression also does not use the return keyword, it implicitly evaluates the expression after: and returns its value
# Lambda expressions are typically used when short, throwaway functions are needed
# Similar to nested functions, lambda expressions can reference variables from containing scope
# To run a lambda expression, you need to follow it with () similar to a function and pass all necessary arguments inside
# This is why, for cleaner syntax, lambda functions are assigned to a variable: in order to make the syntax cleaner when calling

add1= lambda x: x + 1
result= add1(3)
print(result)

add_nums= lambda x, y: x+y
result=add_nums(13, 20)
print(result)


names= ['Ron', 'Andy', 'April']
(lambda names: names.append('Tom'))(names) 
print(names)


# Lambda expressions are most used alongside map and filter which we will look at in upcoming sections