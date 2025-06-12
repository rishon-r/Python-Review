'''
SOME THEORY:

What is threading? - Threading is essentially a concept by which we are allowed to run multiple operations at seemingly
the same time. This helps reduce the time it takes for our programs to run

In Python, we implement threading using the threading module.

What is a thread? - A thread refers to a lightweight subprocess. Multiple threads within the same process share resources and
memory.
( A lightweight subprocess is essentially a subprocess that does not require too many resources to run)

Python's threading module allows concurrent execution of code via multiple threads. 

What is concurrency?- Concurrency is simply the idea of doing multiple things at once. Tasks start, stop and resume over time, 
possibly overlapping in execution.

When discussing concurrency, we must also discuss parallelism.

What is parallelism?- Parallelism refers to the process of doing multiple things at exactly the same time, usually on multiple
CPU coures.

How do concurrency and parallelism differ?- Concurrency dicusses STRUCTURE, Parallelism is about EXECUTION.

Python gives us concurrency, but not true parallelism. This is due to something known as the Global Interpreter Lock (GIL).

To  understand threading further, we need to understand the difference between I/O bound tasks and CPU bound tasks.

What is a CPU bound task?- A CPU bound task is one that requires a lot of CPU cycles. These are essentially tasks that require
intensive computation. Some examples of such tasks are Image Processing and Matrix Multiplication. Such tasks benefit from
multiprocessing not threading.

What is an I/O bound task?- I/O bound tasks are those that wait for external operations such as disk I/O or network requests. These
tasks benefit from threading due to the idea that we can run other threads when one thread is waiting.

Finally, we discuss the idea of Synchronous execution vs Asynchronous execution

What is Synchronous Execution? - In Synchronous execution, code runs line by line. This is simple, but inefficient for I/O 
bound tasks due to the wait times. This is because in Synchronous execution, each operation must complete before the next one 
starts.

What is Asynchronous Execution? - In Asynchronous execution, tasks can pause and allow others to run when waiting. This is very
efficient for I/O bound tasks with many operations.

'''

import threading #we use the threading module to practice threading in Python
import time # we use the time module to illustrate our more complex threading examples


# Now we define the function that the thread will execute, called the target function
def greet():
    print("Hello from a thread")

# Now, we create a thread object (remember not to use brackets when passing the function as a target argument)
t= threading.Thread(target=greet)

# We start the thread using the start() method which tells Python to run the thread in parallel with the main program
t.start()

# We use the join() method in order to wait for the thread to finish. It essentially tells the main program to wait for the thread to finish before proceeding further
t.join()
# Note that join optionally takes a timeout argument which indicates the maximum amount of time the main program will spend waiting for the thread to finish running.
# If the thread is still alive after this, the main thread continues.

#Now, we will view a full example using threading. 

def work():
    print("Worker thread started")
    time.sleep(2)
    print("Worker thread finished")

t=threading.Thread(target=work)

print("Main thread: Starting worker")
t.start()

print("Main thread: Waiting for worker to finish")
t.join()

print("Main thread: done")

# Now, we will try running multiple threads at the same time

def task(task_number):
    print(f"Task thread {task_number} started")
    time.sleep(10)
    print(f"Task thread {task_number} finished")

print("Main thread: Starting task threads")

threads=[] # Creating a list that will eventually hold all started threads
for _ in range(1,5): # Note that _ in Python is used to represent a discarded variable 
    t=threading.Thread(target=task, args=[_]) #args here refer to the arguments being passed to the target function
    threads.append(t)
    t.start()
    

print("Main thread: Waiting for task threads to finish")

for thread in threads:
    thread.join() 

# Why might the output not be in the exact order in which we close the threads?
# This is because when you run multiple threads, they are executed concurrently, and the order in which they complete depends on the operating system's thread scheduler, not the order you started them in.

print('Main thread: All threads finished')


# LOCKING
x= 8192
lock= threading.Lock()


def halve():
    global x, lock
    lock.acquire()
    while x>1:
        x/=2
        print(x)
        time.sleep(1)
    
    print("Minimum reached")
    lock.release()

    

def double():
    global x, lock
    lock.acquire()
    while x < 16384:
        x*=2
        print(x)
        time.sleep(1)

    print("Maximum reached")
    lock.release()

t1= threading.Thread(target=halve)
t2= threading.Thread(target=double)

# This thread will halve the number
t1.start() 
# This thread doubles it
t2.start() 
# Together, they ensure that the number neither reaches the maximum nor minimum 
# This is because when they run concurrently, any time a number is halved it is then doubled by the other thread
# So, usually, the number just reaches a middle of range value and fluctuates slightly
# The above would be the case if we did not use a lock
# Locking in Python threads refers to a mechanism that prevents multiple threads from accessing the same shared resource at the same time
# The lock does not know which resource it is locking/protecting, it is the developers job to place the resource within the lock.acquire() and lock.release() block
# Above, it is the variable x that is the shared resource being protected
# When one thread has the lock, the other cannot access x
# So the number is either halved till a minimum is reached before then getting doubled till a maximum is reached or vice versa
# This is based on which thread acquires the lock first
# The thread that acquires the lock first depends on how the OS schedules the threads — it's not guaranteed to be the one started first.



# SEMAPHORES IN PYTHON

# What is a Semaphore?
# A semaphore is a synchronization tool that controls access to a shared resource pool.
# It does not prevent access completely (like a lock), but rather allows a fixed number of threads
# to access the resource at the same time.

# Think of it like allowing only 5 people into a room at once.
# Others must wait outside until someone leaves and frees up a slot.

# Difference from Locks:
# - A Lock only allows one thread to access a critical section at a time (mutual exclusion).
# - A Semaphore allows multiple threads (up to a specified maximum) to enter.


# CREATE A SEMAPHORE OBJECT


# Use a BoundedSemaphore which, unlike a regular Semaphore, will raise an exception if
# `release()` is called more times than `acquire()`.
# This helps avoid programming bugs where releases happen too many times.
semaphore = threading.BoundedSemaphore(value=5)  # Allow up to 5 threads at a time


# DEFINE A FUNCTION TO SIMULATE ACCESS TO SHARED RESOURCE


def access(thread_number):
    print(f"Thread-{thread_number} is trying to acquire access to the resource...")

    # Acquire the semaphore (decrements the internal counter)
    semaphore.acquire()

    try:
        print(f"Thread-{thread_number} has acquired access!")
        time.sleep(5)  # Simulate some operation (e.g., database query, file write)
    finally:
        print(f"🔓 Thread-{thread_number} is releasing access.")
        # Always release the semaphore (increments the internal counter)
        semaphore.release()

# CREATE AND START MULTIPLE THREADS


# We create 5 threads. All of them will be allowed through,
# but if we increased the count to more than 5, extra threads would have to wait.

for i in range(1, 6):
    t = threading.Thread(target=access, args=[i])
    t.start()

    # Optional: sleep between thread starts to stagger access attempts
    time.sleep(10)  # This makes threads start sequentially instead of all at once




