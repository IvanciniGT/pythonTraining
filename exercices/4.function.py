# Functions in python are a different class of VERBS... They are actions that we can perform in our program.
# Like complex actions... 
# Every single programming language comes with a bunch of predefined functions.
# In python, we have a bunch of predefined functions.

# And usually every single programming language allows us to create our own functions.

# Right now I'm not going to show you how to create a function... I'm going to show you how to use them.

# In python we have:

print("Hello, World!")  # This prints a message to the console.
                        # ^^^^^ Semantics ^^^^^ What print function does? is to print a message to the console.
 # ^^^^^ SYNTAX

# To execute a function we have to write the name of the function followed by a pair of parenthesis.
# Some functions require some arguments... and we have to pass them inside the parenthesis.
# If our function requires a bunch of arguments, we have to separate them with commas.

# Some built-in functions in python are:
#- print                 # Prints a message to the console
#- input                 # Reads a message from the console
#- len                   # Returns the length of a collection
my_list_1 = [1, 2, 3]
print(len(my_list_1))       # This would print 3

#- type                  # Returns the type of a value (data type)
print(type(1))             # This would print <class 'int'>
print(type(1.0))           # This would print <class 'float'>
print(type("Hello"))       # This would print <class 'str'>
print(type(True))          # This would print <class 'bool'>
print(type([1, 2, 3]))     # This would print <class 'list'>

# In addition we have functions to switch between data types.
#- int                   # Converts a value to integer... when possible
a_decimal_number = 1.5
print(int(a_decimal_number))            # This would print 1

an_integer_number = 1
print(float(an_integer_number))           # This would print 1

a_text_containing_a_number = "19.8"

# We can convert a string containing a number to a number
print(float(a_text_containing_a_number))  # This would print 19.8
print(int(float(a_text_containing_a_number)))  # This would print 19.8

number1 = 19
print("Your number is " + str(number1)) # "Your number is 19"


# age is gonna point to whaerver the user inputs in the console... But.. in a console, users write TEXT
# So.. if we type: 19... age variable is gonna point to the string "19"
age = input("How old are you? ") # This would print "How old are you?" and wait for the user to type something.
print("You are " + age + " years old.") # This would print "You are <age> years old."
age = int(age) # This would convert the string "19" to the integer 19
age += 1
print("Next year you will be " + str(age) + " years old.") # This would print "Next year you will be <age> years old."

# As you have seen... some function return a value... and we can use that value to do something else.
# Such as the function input... it returns the value that the user inputs in the console.