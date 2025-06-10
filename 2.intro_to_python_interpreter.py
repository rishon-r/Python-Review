# As discussed before, Python is an interpreted language which means it is executed line by line 
# The Python interpreter is usually installed in usr/local/bin and adding this to the PATH global variable in the command line makes it possible to access the python interpreter at the command line
# You can do the above by typing in python3 in command line
# You exit the Python command line interpreter by typing ctrl + z using an exit code 0 status. You can also type in the quit() command

# The python interpreter is a program in and of itself and works somewhat similar to the unix shell
# i.e when called with standard input connected to a tty device, it reads and executes commands interactively; when called with a file name argument or with a file as standard input, it reads and executes a script from that file.

# There is a second way of staring the python interpreter: python -c command [args] ...
# This executes the statements in command in a manner analogous to the shell's -c option
# Eg; python -c "print('hello world)"    prints hello world
# It is important to wrap the command in quotes as a lot of the symbols used in Python statements are special characters to the shell and may cause oit to go berserk

# Some python modules are also useful as scripts
# These can be invoked using python -m module [arg] ..., which executes the source file for module as if you had spelled out its full name on the command line.
# E.g python -m module_name
# You can also use the -i flag instead which will run the script and then go into interactive mode after
# E.g python -i myscript.py

# PASSING ARGUMENTS
# The script name and arguments passed are turned into a list of strings once known to the interpreter and are assigned to the argv variable in the sys module
# This list is of length atleast 1 and if no script name or arguments are passed then sys.argv[0] is an empty string
# When the script name is given as '-' (meaning standard input), sys.argv[0] is set to '-'. When -c command is used, sys.argv[0] is set to '-c'.
# When -m module is used, sys.argv[0] is set to the full name of the located module.

# NOTE: TTY stands for teletypewriter and in linux terms it basically just means a terminal (A physical device capable of typing in input and receiving output)

# INTERACTIVE MODE: The Python interpreter is said to be in interactive mode when commands are being read from a tty
# When in interactive mode the Python Interpreter prompts for new commands using the primary prompt (the three arrows >>>) and prompts for continuation lines of commands with the secondary prompt (three dots ...)

# By default, Python source files are treated as encoded in UTF-8
# To declare an encoding other than the default one, a special comment line should be added as the first line of the file. The syntax is as follows: -*- coding: encoding -*-
# Here, encoding is one of the valid codecs supported by Python
# THis line is always the first line of a Python file unless there is a UNIX shebang line in which case this is the second line




