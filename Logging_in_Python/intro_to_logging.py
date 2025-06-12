# The logging module is a built-in Python module that provides a flexible framework
# for emitting log messages from Python programs. Logging is crucial for understanding
# the flow of a program, diagnosing issues, and tracking events that happen during
# the execution of your code — especially in larger, more complex systems.

# To make use of the logging features, you first need to import the logging module:
import logging

# CONFIGURING THE LOGGING SYSTEM


# By default, Python's logging module is configured to handle only messages that are
# WARNING level or higher (i.e., WARNING, ERROR, and CRITICAL). Lower-severity messages
# like INFO and DEBUG are ignored unless we explicitly reconfigure the logging system.

# The logging system can be customized using logging.basicConfig().
# This function allows us to define the minimum severity level of messages
# that should be processed and shown by the logging module.

# Here, we set the logging level to INFO, which means that any log messages
# of level INFO and above (INFO, WARNING, ERROR, CRITICAL) will be displayed.
# DEBUG messages will still be ignored.
# The filename below represents the file in which we ant our logging statements to be written
# It will be created when this is called
# We can also mention a format alongside basicConfig
# These format codes can be viewed under LogRecord attributes in the logging section of thePython documentation 
logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# LOGGING LEVELS IN PYTHON


# Python's logging module defines five standard logging (security) levels,
# each representing the severity or importance of a logged message.

# 1. DEBUG (Lowest level of severity)
#    - Used for detailed diagnostic information.
#    - Ideal when debugging the internal flow of the program or for testing purposes.
#    - Typically of use only when diagnosing problems
#    - Example: "Entered the authentication function with user_id = 42"

# 2. INFO
#    - Used for general information about program execution that might be useful to end users or developers.
#    - These are *normal* events — not errors, just informative messages.
#    - Usually used for confirmation that things are working as expected
#    - Example: "You have 5 new notifications", "User successfully logged in"

# 3. WARNING
#    - Indicates a potential problem or unexpected situation that is not an error — yet.
#    - It's a heads-up that something could go wrong if not addressed.
#    - The software is still typically working as expected
#    - Example: "Disk space running low", "API rate limit approaching"

# 4. ERROR
#    - Used to report errors that occurred during execution, typically due to an exception or unexpected condition.
#    - The program may still continue running, but this message indicates something went wrong.
#    - Example: "Failed to save file due to permission error"

# 5. CRITICAL (Highest level of severity)
#    - Used when a serious error has occurred that could prevent the program from continuing to run correctly.
#    - Example: "Database server is down", "Core service has failed — shutting down system"

# EXAMPLE LOGGING OUTPUT
# Since we set the logging level to INFO, the following message will be printed.
logging.info("You have 20 new emails!")

# This is a more severe message (CRITICAL), and will also be shown:
logging.critical("Key component A has failed!")

# BEHAVIOR WITHOUT CONFIGURATION

# Note: If you had not set the logging level using logging.basicConfig(level=logging.INFO)
# earlier in the code, the logging system would have used the default level, which is WARNING.
# In that case, the logging.info() message would not have been printed, and only messages
# at the WARNING level and above would have been shown.



# In summary:
# - The logging level acts as a filter. It determines the minimum severity of messages to be shown.
# - Messages with a lower severity than the configured level are ignored.
# - Python's default logging level is WARNING, so only WARNING, ERROR, and CRITICAL messages
#   are displayed unless you lower the level explicitly (e.g., to INFO or DEBUG).


# FINAL NOTES

# The logging module is preferred over using print() statements for debugging and monitoring,
# because it allows fine-grained control over what is logged, how it is formatted,
# where it is output (e.g., to console, file, or network), and what severity levels are included.





