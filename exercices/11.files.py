
# We will write a file... with some contents in it

# We will read the file and print its contents to the console

i_have_a_text = """
This is a text file
containing some text
and some numbers
and configuration data


and...
a bunch of other stuff
"""

# We want to store that text in a file
file_name = "my_text_file.txt"

# In previous versions of python... we had to close the channel manually, after we were done with it.
# We also had to handle exceptions... in case something went wrong.

# Exception: An exception is something that happens during the execution of a program that disrupts the normal flow of the program's instructions.
# Exceptions are raised when the interpreter detects an error in the program execution:
# - We cannot open the file because you do not have the permissions to do so
# - The file does not exist
# - The file is locked by another process

# There is no way to know in advance if an exception is going to be raised or not...
# All we know is that it could be raised... and we have to be prepared to handle it.

try:
    my_channel = open(file_name, "w")
    my_channel.write(i_have_a_text)
except Exception as e:
    # Here we could specify the logic to handle the exception
    print("An error occurred: ", e)
finally:
    # and it does not matter if an exception was raised or not... 
    # Anyway... i want you (PYTHON) to execute this code below
    my_channel.close()


#my_channel = open(file_name, "w")
#my_channel.write(i_have_a_text)
#my_channel.close()
# But in this case... if an Exception is thrown... my program will break at runtime.
# That's not what we want... we want to handle the exceptions carefully.
# We may need the program to continue running even if an exception is raised.
# Or... depending on the use case.. we may need the program to leave (finish) gracefully.


# Nowadays we can just make use of that with...as syntax... 
# that will take care of closing the channel for us
# and also will take care of handling exceptions
# If an exception is raised... the channel will be closed automatically

# open is a built-in function in python
# It allows us to open a connection against a file
# The first argument is the name of the file
# The second argument is the mode in which we want to open the file
# In this case "w" means write.... When writing a file... we will rewrite the file if it already exists... completely deleting its contents
# We can also open a connection (channel) in read mode... "r"
# We can also open a connection in append mode... "a"
with open(file_name, "w") as my_channel:
    # The write method of the channel object allows us to write data to the file
    my_channel.write(i_have_a_text)

# And that's all.

# In order to read a file... we can do exactly the same... but in read mode
with open(file_name, "r") as my_channel:
    # Through the channel... i will be able to read the contents of the file.... 
    # line by line... or the whole file at once
    # Let's read first the file as a whole
    file_contents = my_channel.read()
    print("Here's the content of the file:")
    print(file_contents)

# We can also read the file line by line
with open(file_name, "r") as my_channel:
    print("Here's the content of the file (line by line):")
    for line in my_channel:
        print(line, end="")


# Regarding files.. let me show you a python module that is extremely useful
# The os module
# That module allows us to manage folders and files in the operating system

import os

my_file_exists=os.path.exists(file_name) # This will return True if the file exists... False otherwise
print("The file exists: ", my_file_exists)

my_sub_folder_name = "subfolder"
my_sub_folder_exists=os.path.exists(my_sub_folder_name) 
if(not my_sub_folder_exists):
    os.mkdir(my_sub_folder_name) 

if(my_file_exists):
    os.rename(file_name, my_sub_folder_name + "/" + file_name)
    print("The file has been moved to the subfolder")

os.remove(my_sub_folder_name + "/" + file_name)
print("The file has been removed")