
# In python files we can add comments... like this one: LINE COMMENT

# Most programming language allow to introduce block comments 
# with /* and */. Python does not have this feature.
# We cannot have multi-line comments in python. (But there is a workaround)

# In python we have a bunch of predefined data types.
# The most common ones are:
# Texts: str

"Hello, World!" # This is a string
'Hello, World!' # This is also a string

# Well... python is not that stupid! And it knows that we cannot (there is no way) to recover those strings in the future...
# So it is ignoring them...

"""
Multiline text
can be created using triple quotes
"""

'''
Multiline text
can be created using triple quotes
''' # We can enclose strings with triple quotes to create multiline strings... 
# and actually as python is going to ignore them, we can use them as comments! TRICK !

# Numbers: int, float, complex

1 # This is an integer
1.0 # This is a float
1 + 1j # This is a complex number

# Booleans: bool
True # This is a boolean
False # This is a boolean


# All those are called scalar types. 
# They are the most basic data types in python.

# There are also some compound data types: COLLECTIONS... And there is a bunch of them!

# Tuple: tuple
(1, 2, 3) # This is a tuple of integers
(1.0, 2.0, 3.0) # This is a tuple of floats
(1 + 1j, 2 + 2j, 3 + 3j) # This is a tuple of complex numbers
("Hello", "World") # This is a tuple of strings
(True, False) # This is a tuple of booleans

# Tuples pack values together. They are INMUTABLE. We cannot change the vales of a tuple once it is created.
# We cannot even add or remove elements from a tuple. We can only get the values of a tuple.

# List: list
[1, 2, 3] # This is a list of integers
[1.0, 2.0, 3.0] # This is a list of floats
[1 + 1j, 2 + 2j, 3 + 3j] # This is a list of complex numbers
["Hello", "World"] # This is a list of strings

# Lists are like TUPLES... but they are MUTABLE. We can change the values of a list once it is created.
# We can add or remove elements from a list.... update elements... etc.

# Dictionary: dict
{"key1": "value1", "key2": "value2"}

# A diccionary is a collecion of values packed together where each element can be accessed by a key.
# When using lists or tuples we access the elements by their position in the list or tuple.

# If you think about that, a dictionary is a list where the element keys are a sequence of integers starting from 0.

{ 0: "value1", 1: "value2" }
# That dictionary is equivalent to the list ["value1", "value2"]


{"ip": "192.168.23.47", "port": 80, "protocol": "http"} # Web service information
{"port": 80, "ip": "192.168.23.47", "protocol": "http"} # Web service information

    # You could tell python. Ey! give me the "ip" of that server
    # Give me the "port" of that server

["192.168.23.47", 80, "http"] # Web service information
["http", "192.168.23.47", 80] # Web service information

    # You could tell python. Ey! give me the 1st element of that list. It's up to you to know that the 1st element is the "ip"
                               # Give me the 3rd element of that list