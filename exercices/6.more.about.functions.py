
# Python comes with a set of predefined functions... 
# In order to execute them we have to write the name of the function 
# followed by a pair of parenthesis.

# Case the function requires some arguments... we have to pass them inside
# the parenthesis. If our function requires a bunch of arguments, we have to
# separate them with commas.

print("Ey! this is the first argument", "Ey! this is the second argument")

# The point here... is that python allows us to create our own custom functions.
# It's extremely easy to create a function in python.

def my_function_name(): # We were just defining the function
    print("This is the first statement belonging to the function")
    print("This is the second statement belonging to the function")
    print("This is the third statement belonging to the function")
# Be careful when indenting... 
# A tab is not the same as 2(4) whitespaces... even though it could look the same in you editor.

def my_function_name2(): # We were just defining the function
        print("This is the first statement belonging to the function")
        print("This is the second statement belonging to the function")
        print("This is the third statement belonging to the function")


my_function_name() # Here we are executing the function

my_function_name2() # Here we are executing the function

my_function_name() # Here we are executing the function


def say_hello( name ):
    print("Hello " + name + "!")

say_hello("Ivan")
say_hello("Brenda")
say_hello("Luca")

                               # Default value, whenever the user does not provide a value for the argument.
def say_good( name = "dude", is_it_late = False ):
    if is_it_late:
        print("Good evening " + name + "!")
    else:
        print("Good morning " + name + "!")

say_good("Ivan", False) # both arguments are provided
say_good("Brenda", True)

say_good("Luca")        # only one argument is provided
say_good()              # no argument is provided
# When we have several arguments with a default value set, we can provide a value for whichever argument we want just by providing the name of the argument and the value we want just by naming the argument before the value.
say_good(is_it_late = True) # This is what we called "named arguments"


# Some functions will run the code that is inside the function... and that's all!
# Such as the functions we have created so far.

# But.. in some situations we want the function to return a value.

# Imagine this function:

def twice_value( value):
     return value * 2

result = twice_value(5)
print(result) # This would print 10

print(twice_value(10)) # This would print 20

def generate_greeting( name , is_it_late = False):
    if is_it_late:
        return "Good evening " + name + "!"
    else:
        return "Hello " + name + "!"
    
def generate_greeting_3( name , is_it_late = False):
    return "Good evening " + name + "!" if is_it_late else "Hello " + name + "!"
    
# Note: USUALLY it is not considered a good practice to have more than 1 return statement in a function.
# Actually it is considered a bad practice to have more than 1 return statement in a function.
# Why? Because it makes the code harder to read and understand.

# The good practice is to have only one return statement in a function.
def generate_greeting2( name , is_it_late = False):
    greeting_to_return = ""
    if is_it_late:
        greeting_to_return = "Good evening " + name + "!"
    else:
        greeting_to_return = "Hello " + name + "!"
    return greeting_to_return

generated_greeting = generate_greeting("Ivan", True)
print(generated_greeting) # This would print "Good evening Ivan!"
generated_greeting = generate_greeting("Brenda", False)
print(generated_greeting) # This would print "Hello Brenda!"