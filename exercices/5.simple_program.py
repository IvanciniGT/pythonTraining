
# I want to ask the user for his/her name and age.
# And then I want to say hi to the user and 
# tell him/her how old he/she is.

name = input("What is your name? ")
age = input("How old are you? ")

print("Hi " + name + "!")
print("You are " + age + " years old.")


# I want to inform the user if he/she can drive a car or not:       16
# I want to inform the user if he/she can vote or not.              18
# I want to inform the user if he/she can drink alcohol or not:     21

# Flow control: if, elif, else
# Sometimes we do not want the computer to execute every single line of code.
# They need to be executed under certain conditions.

## IF STATEMENT... the simplest form of flow control.
# if <boolean_value>:
#    The code that is going to be executed if the boolean value is True.

age = int(age)

if age >= 21:   # Conditional operator
    print("Ey! With your current age you can drive a car and vote and you can drink alcohol" ) # Statement
    print("Congratulations (kind of...!)") # Statement
elif age >= 18:   # Conditional operator
    print("Ey! With your current age you can drive a car and vote" ) # Statement
    print("Congratulations!") # Statement
elif age >= 16:   # Conditional operator
    print("Ey! With your current age you can drive a car" ) # Statement
    print("Congratulations!") # Statement
else:
# if age < 16:    # Conditional operator
    print("Sorry! You are too young to drive a car" ) # Statement
    print("Come back in " + str(16 - age) + " years.")

# IF EXPRESSION
# An if expression is an EXPRESSION

number = 10 # Imagine that this could be a random number (or that we ask the user for a number)
is_that_number_odd = True if number % 2 == 1 else False
                     ################################## this is an expression... It will return TRUE or FALSE... depending on the condition

# The code above is equivalent to:  

if number % 2 == 1: # IF as a statement... it allows to execute Statements inside the block
    is_that_number_odd = True # Statement
else:
    is_that_number_odd = False

# This brings us the concept of cyclomatic complexity:
# The number of different paths that can be taken through when running a program.

# In our example is 4

# Loops
# Sometimes we want to execute a block of code multiple times.
person  = { "name": "Ivan"  , "age": 48 }
person2 = { "name": "Brenda", "age": 20 }
person3 = { "name": "Luca"  , "age": 17 }
person4 = { "name": "Jane"  , "age": 9  }
people  = [ person, person2, person3, person4 ]

    # This is a variable... that I define
    ###########
for my_var in people:
    age = my_var["age"]  # myvar is gonna point to person, then person2, then person3, then person4
    if age >= 21:   # Conditional operator
        print("Ey! With your current age you can drive a car and vote and you can drink alcohol" ) # Statement
        print("Congratulations (kind of...!)") # Statement
    elif age >= 18:   # Conditional operator
        print("Ey! With your current age you can drive a car and vote" ) # Statement
        print("Congratulations!") # Statement
    elif age >= 16:   # Conditional operator
        print("Ey! With your current age you can drive a car" ) # Statement
        print("Congratulations!") # Statement
    else:
    # if age < 16:    # Conditional operator
        print("Sorry! You are too young to drive a car" ) # Statement
        print("Come back in " + str(16 - age) + " years.")

my_numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in my_numbers_list:
    print("Number: "+str(number))

# That is a foor loop as a statement... 
# It allows to execute Statements for each element in the collection

# We can also use a for loop as an expression...
my_new_numbers_list = [ number * 2 for number in my_numbers_list ]
                      # Create a new list containing the double of each element in the original list

# We are just learning python SYNTAX!

# In this first kind of loop that we have seen, we always loop through a collection of elements.
# Imagine wea want to do a task... let's say 25 times... In order to do that 
# we have to create a collection with 25 elements... 
# and then loop through that collection.

for iteration_number in range(25,0,-2):
    print("Doing a task...."+ str(iteration_number))

# Another kind of loop: while loop.
# While loops have the same structure as if statements.
# while <boolean_value>:
#     The code that is going to be executed while the boolean value is True.

# The difference with an if statements, is that the condicion is not going to be ever evaluated just once.... 
# but until the condition is False.

max_number = 25
current_number = 1

while current_number <= max_number:
    print("Doing a task...."+ str(current_number))
    current_number += 1

print("The task is done!")

print(list(range(0,10)))