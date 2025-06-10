# The print() function
# The print() function in Python is used to display output to the console.
# It can take any number of arguments and prints them with a default space between them.
# The syntax is:
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# BASIC USAGE
print("Hello", "world")
# Output: Hello world
# By default, print separates each argument with a space (' ')
# and ends the line with a newline character ('\n')
# USING 'sep' PARAMETER
print("apple", "banana", "cherry", sep=", ")
# Output: apple, banana, cherry
# 'sep' stands for separator — it defines what to place between multiple objects passed to print() (default value is the spce character)
print("2025", "05", "26", sep="-")
# Output: 2025-05-26
# Useful when printing dates, file paths, or other formatted text
# USING 'end' PARAMETER (default value of end parameter is '\n')
print("Loading", end="...")
# Output: Loading...
# 'end' replaces the default newline with a custom string
print("done!")
# Output continues on the same line because the previous print() ended with "..." instead of a newline
# COMBINING 'sep' AND 'end'
print("A", "B", "C", sep="-", end=" END\n")
# Output: A-B-C END
# 'sep' controls how the values are joined, 'end' controls what comes after
# PRINTING WITHOUT NEWLINE
print("First part", end=" ")
print("Second part")
# Output: First part Second part
# Both print statements appear on the same line because of custom 'end'
# PRINTING WITH NO SEPARATOR
print("a", "b", "c", sep="")
# Output: abc
# Useful for joining values with no space
# PRINTING WITH SPECIAL CHARACTERS
print("Line 1", end="\n---\n")
print("Line 2")
# Output:
# Line 1
# ---
# Line 2
# Here we use a custom end to insert a divider between two print outputs
