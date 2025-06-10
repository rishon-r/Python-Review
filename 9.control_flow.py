# IF STATEMENT
# The if statement is the most basic control flow statement available
# It executes a set of statements once if a condition is True
# The most basic form of the if statement consists of the if statement alone and this does nothing if the condition is not true
# If we want to execute some statements if the condition is False, we use the else statement
# The statements under the if and else statements are indented and are said to be a part of the if block and else block respectively
# Python does not use brackets but instead indentation and colons to differentiate between different blocks of code
# Example:
a=7
b=4
if a>b:
    print("Hello")
else:
    print('hi')

# If there are a series of intermediate conditions we also want to check, we can us the elif block for that.
# We can use as many elif blocks as required within a particular set of if-elif-else statements
# Note that all elif blocks and the else block are optional with the if statement
# Example: 
num= 70

if num > 90:
    print('A')
elif num > 80:
    print('B')
elif num > 70:
    print('C')
elif num > 60:
    print('D')
elif num>0:
    print("FAIL")
else:
    print("ERROR")

# It is also possible to nest if statement within each other
# An if, elif or else block can have multiple nested if statements within it

#E.g

color="red"
num=5

if num>3:
    if color=="red":
        print("Success")
    else:
        print("Failure")
elif num>2:
    if color=="red":
        print("Success")
    else:
        print("Failure")
else:
    print("Failure")

# MATCH Statements
# A match statement is superficially analogous to the switch case in Java or C
# It takes an expression and checks if that expression matches up with a series of different values (should be literals), each labelled by case
# At the point of the first match, the statements under that respective case will be executed
# The variable _ is a wildcard and never fails to match. Use it as the analogue for the default statement in switch case
# The or symbol | can also be used to help assess multiple values in a given case
# Example below:
status=409

match status:
    case 404:
        print("ERROR TYPE !")
    case 401 | 403:
        print("ERROR TYPE 2")
    case _:
        print("NEW ERROR!")

