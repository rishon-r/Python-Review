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

# A StreamHandler sends log messages to a stream — by default, this is sys.stderr (the console).
# This is useful for immediate feedback during development or for logging runtime events in real time.
# Unlike the FileHandler (which persists logs), the StreamHandler simply displays them on-screen.
stream_handler = logging.StreamHandler()

# We can set level for stream handler and file handler as well separately
# This will allow us to choose the security level of messages that go into the file and directly to console respectively
stream_handler.setLevel(logging.DEBUG) # Allowing stream handler to handle debug messages

# Define a formatter that specifies the log message format.
# Here, each log will include:
# - the current timestamp (asctime)
# - the log level (levelname)
# - the actual log message (message)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Define a simpler format for console output
stream_formatter = logging.Formatter("%(levelname)s: %(message)s")

# Attach the formatter to the file handler so that the log messages are written in the specified format.
file_handler.setFormatter(formatter)

# Attach the formatter to the stream handler
stream_handler.setFormatter(stream_formatter)

# Add the file handler to the logger.
# This step "plugs in" the handler so that the logger knows where and how to output log messages.
logger.addHandler(file_handler)
logger.addHandler(stream_handler)  # Show logs on console

# Log a message at INFO level.
# Since we've set the logger's level to INFO, this message will be written to 'sample.log'.
# It will also be printed to console
logger.info("Logger object Created")
