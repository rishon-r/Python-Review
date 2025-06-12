import logging  # Import the built-in logging module

# CREATING A CUSTOM LOGGER

# Create a custom logger using getLogger().
# By convention, we pass __name__ to associate the logger with the current module's name.
# This helps in larger projects where logs from different modules can be identified.
logger = logging.getLogger(__name__)

# Set the minimum severity level for this logger to INFO.
# This means only log messages with level INFO or higher (INFO, WARNING, ERROR, CRITICAL) will be handled.
logger.setLevel(logging.INFO)

# Create a FileHandler object to write log messages to a file named 'sample.log'.
# This handler is responsible for directing the log output to a file.
file_handler = logging.FileHandler('sample.log')

# Define a formatter that specifies the log message format.
# Here, each log will include:
# - the current timestamp (asctime)
# - the log level (levelname)
# - the actual log message (message)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Attach the formatter to the file handler so that the log messages are written in the specified format.
file_handler.setFormatter(formatter)

# Add the file handler to the logger.
# This step "plugs in" the handler so that the logger knows where and how to output log messages.
logger.addHandler(file_handler)

# Log a message at INFO level.
# Since we've set the logger's level to INFO, this message will be written to 'sample.log'.
logger.info("Logger object Created")