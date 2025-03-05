import time # We are importing the time module
            # that module defines a function called sleep
            # that function will allow us to pause the execution of the program for a while

            # But the truth is that a program does not execute itself.
            # Threads execute programs.
            # What the pause function actually does is to tell the thread that is 
            # executing the program to stop executing the program for a while.

# The definition of what a "thread" is in python is in CLASS called Thread...
# But that program is defined in a module called threading
import threading
# Someone who can count

              # Here we say to python... A Counter is a Thread... with a custom behavior
class Counter(threading.Thread):
    # If a counter is a Thread... it will inherit all the attributes and methods of the Thread class
    # as defined in the threading module
    # We can also define new attributes and methods for the Counter class

    # The Thread class of python threading module has a method called start().
    # That method allows us to start the execution of the thread.... to start its life cycle....
    # Completely independent from the main thread of the program.

    # In python, as defined in the Thread class of the threading module, 
    # the start method will call internally a method called "run"... that should be defined in the Thread class.
    # The code inside the run method is the code that will be executed by the thread.... in parallel with the main thread.

    # From the main thread we will call the "start" method of the thread object.
    # And internally, python creates a new OS THREAD... that will execute the code defined in the run method.

    # Actually the Thread class already has a run method defined... but that implementation is empty.
    # We can override that method with our own implementation: THE TASK that we want the new thread to execute.


    # The constructor of the class
    def __init__(self, name, max_value, delay):
        # whenever a class extends another class... It is mandatory to call the constructor of the parent class
        super().__init__()
        self.name = name
        self.max_value = max_value
        self.delay = delay

    def start_counting(self):
        self.start()
    
    def run(self): # This overrides the default implementation of the run method in the Thread class
        for number in range(1, self.max_value + 1):
            print("I am counter " + self.name + " and I am counting " + str(number))
            # After counting one number, we want to chill for a while (that delay)
            # Python already has a function for that... similar to the sleep command in linux.
            time.sleep(self.delay)
            # The sleep function is defined in the `time` module
            # In order to use it, we have to import the module first

my_first_counter = Counter("A", 10, 1)
my_second_counter = Counter("B", 20, 0.5)
my_third_counter = Counter("C", 15, 2)

# Who is executing this code below??? The main thread... Every single line of code is executed by a thread
my_first_counter.start_counting()
my_second_counter.start_counting()
my_third_counter.start_counting()

# Question 1: Who will execute this line of code? MAIN_THREAD
# Question 2: When this line of code will get executed? (When the HI message will shop up?)
# This line will get executed when the main thread reaches this line of code.... 
# And the main thread is wait for the other threads to finish their work?? NO
print("HI")
# Maybe we could wait for some of them...
my_first_counter.join() ## This makes the main thread to wait for the first counter to finish (actually for the run method of the first counter to finish)
                         # Thats how we synchronize threads
print("First counter is done")
my_second_counter.join() ## This makes the main thread to wait for the first counter to finish (actually for the run method of the first counter to finish)
print("Second counter is done") 
my_third_counter.join() ## This makes the main thread to wait for the first counter to finish (actually for the run method of the first counter to finish)
print("Third counter is done")
print("All counters are done... we can leave now")
# The join function is defined in the Thread class of the threading module
# Our Counters inherit that function from the Thread class


# NOW We could make a program (SCRIPT) that checks the status of our services ...
# Not one by one... but in parallel
# Ey .. maybe I have 200 services.. and I want to check them 5 by 5
# I can create 5 threads... each one checking 1 service at a time
# And split the work between them... I will give 200/5 = 40 services to each thread

# That means, my program will finish in 1/5 of the time that it would take to check all the services one by one