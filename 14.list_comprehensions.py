# LIST COMPREHENSIONS

# List comprehensions provide a fast way to create new lists
# This is especially true when the new list to be created consists of elements of another sequence that are changed a bit
# Example: (The below 2 pieces of code do the same thing)

# PIECE 1
li=[]
for x in range(5):
    li.append(x**3)
print(li)

#PIECE 2
new_li= [x**3 for x in range(5)]
print(new_li)

# A list comprehension involves brackets containing an expression followed by a for statement, then zero or more for and if statements
# As a result it returns a list which is a result of evaluating the expression with respect to the for and if statements that follow it
# Another example:

li= [1,2,3,4,5,6,7,8]

even_li= [x for x in li if x%2==0] # Is a list consisting of only the even numbers from li
print(even_li)

# As mentioned above, we can use multiple for statements in a list comprehension
# The below 2 pieces of code mean the same

# PIECE 1
li=[]
for x in range(10):
    for y in ('hey', 'by', 'hello'):
        if len(y)==x:
            li.append((y,x))
print(li)

#PIECE 2
new_li= [(y, x) for x in range(10) for y in ('hey', 'by', 'hello') if len(y)==x]
print(new_li)

# NESTED LIST COMPREHENSION
# The first expression in a list comprehension can be any expression including another list comprehension
# Example: Construction a 3x5 matrix with numbers 1-5 in each row

li= [[x for x in range(1,6)] for i in range(3)]
print(li)

# Example: Construction a 3x5 matrix with numbers 1-15 
li= [[x+ 5*i for x in range(1,6)] for i in range(3)]
print(li)

