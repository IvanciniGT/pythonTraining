
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
