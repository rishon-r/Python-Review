import threading
import time

# EVENTS AND DAEMON THREADS


# 🔹What is an Event in Python?
# An Event is a threading synchronization primitive that allows threads to communicate with each other.
# A threading synchronization primitive is a basic tool or mechanism provided by a programming language (like Python) to help coordinate
# the execution of multiple threads so they don’t interfere with each other when accessing shared resources.
# One thread can wait*for an Event to be triggered (set), and another thread can signal that the Event has occurred.

# Why Use Events?
# Events are useful when:
# - You want one or more threads to pause and wait for a signal before proceeding.
# - You want to decouple the timing of threads — e.g., wait until the user presses a button, or until a task completes.

# Creating an Event
# The Event object is initially in an unset (False) state.
event = threading.Event()

# THREAD FUNCTION THAT WAITS FOR EVENT TO BE SET


def myfunction():
    print("Waiting for the event to be triggered...")
    
    # event.wait() blocks the thread here until event.set() is called
    event.wait()
    
    # Once the event is set, this thread proceeds
    print("Event triggered! Now performing action XYZ...")

# CREATE A NEW THREAD TO RUN THE FUNCTION

# This thread will wait for the event
new_t = threading.Thread(target=myfunction)

# Start the thread
new_t.start()

# MAIN THREAD PROMPTS USER TO TRIGGER THE EVENT


# Simulating an external condition (e.g., user input) to trigger the event
prmpt = input("Do you want to trigger the event? (y/n): ")

if prmpt.lower() == "y":
    # event.set() sets the internal flag to True, allowing waiting threads to proceed
    event.set()
    print("Event has been set!")
else:
    print("Event not triggered. The waiting thread will remain blocked.")

# DAEMON THREADS

# WHAT IS A DAEMON THREAD? - A daemon thread is a background thread that
# automatically exits when all non-daemon (main/foreground) threads have finished running.

# Think of daemon threads like supporting background services 
# they run as long as the main program is alive, but they don’t block the program from exiting.

# KEY IDEA
# MAIN THREAD: Your Python program starts with one main thread.
# REGULAR THREADS: These threads must finish before your program can exit.
# DAEMON THREADS: These threads do NOT block the program from exiting.
# As soon as all non-daemon threads are done, daemon threads are abruptly killed — even if they’re mid-task.

def daemon_task():
    while True:
        print("Daemon thread is running in the background...")
        time.sleep(1)

def regular_task():
    print("Main task is running")
    time.sleep(3)
    print("Main task is done")

# Create daemon thread
d = threading.Thread(target=daemon_task)
d.daemon = True  # Set as daemon before starting
d.start()

# Create non-daemon (regular) thread
t = threading.Thread(target=regular_task)
t.start()

t.join()  # Wait for regular thread to finish
print("Main program exiting. Daemon thread will be killed.")


