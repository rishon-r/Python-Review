# Module example
# You can usually place import statements here

#  A module can have functions
def add(a,b):
    return a+b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

# A module can hold names
var1= "hello"
var2= "world"

if __name__=="__main__":
    # The below code allows the example module to be run as a script wwith 2 arguments passed
    # if done so, it will print the sum of two numbers passed as arguments
    # try an example in the shell
    import sys
    num1= int(sys.argv[1]) # All arguments are stored in sys.argv as strings
    num2= int(sys.argv[2])
    print(add(num1, num2))
    # if the module is imported, the above code is not run