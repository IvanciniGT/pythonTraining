# Procedural programming

def greet(name):
    print("Hello "+name)

greet("Ivan")

# Functional programming: 

# When a programming language allows us to point a variable to a function
# and to execute that function by using that variable

my_function = greet # Am I executing this "greet" function here? NO
                    # Why not? I'm not using parenthesis right after the function name
                    # I'm just assigning my var to the function

# Now... that my var point towards the function... 
# I can execute the function by using the var
my_function("Brenda")  # Here... I'm not executing the my_function var...
# A var cannot be executed!
# What I'm doing is to execute the function that my var is pointing to.


# This function resposibility is to print a greeting message... to the supplied name
def print_greeting(name, greeting_generator_function):
    greeting = greeting_generator_function(name)
    print(greeting)

    # Sometimes, when we create a function, we don't know (or maybe it not our responsibility) 
    # how something needs to be done... I mean... Part of the LOGIC 
    # that needs to be executed by the function is ignored by the function itself.
    # And we supply that logic (the supplied function) as an argument to the function.

def formal_greeting_generator(name):
    return "Good morning "+name

def informal_greeting_generator(name):
    return "What's up "+name

print_greeting("Ivan", formal_greeting_generator)
print_greeting("Brenda", informal_greeting_generator )


def twice( number ):
    return number * 2

# I'm just DEFINING A FUNCTION that receives a number and returns that number multiplied by 2

my_list = [1, 2, 3, 4, 5]

# One build-in python function is the `map` function
# That function requires 2 arguments:
# - A function... that will we used to transform the elements of the collection
# - A collection of elements

new_list = map(twice,my_list)


# The map function is going to create a new COLLECTION
# containing the result of applying the function to each element of the original collection

# So.. It allows me to transform the elements of a collection .
# That is its responsibility.

# But... to transform how? How are elements going to be transformed?
# That is not the responsibility of the map function...
# The map function says... YOU GIVE ME THE TRANSFORMATION FUNCTION... 
# and I will apply it to each element of the collection.
# Afterwards... we decide in which type of collection we want to store the results.
print(new_list)
print(tuple(new_list))

#new_list = map(twice,my_list)
print(list(new_list))

# Map function is part of a wider set of functions that we have not only in python...
# But in almost every single programming language: MAP-REDUCE functions.

# Map-Reduce functions allows us to write map-reduce algorithms.
# It is a different model (approach) to solve problems.

# Tweeter

# All the tweets created worldwide during the last 3 seconds.... A BUNCH OF TWEETS
# Let's say I store them all in a collection... a list of tweets:

# TWEETS
# ------------------------------------------------------
# Playing with my dog #dog #fun #dogLover
# I love my dog #dog #dogLover
# I love my cat #cat #catLover
# I have the best family (my family)#family #love
# Hate school @John #school #hate #schoolIsAFuckingShit
# ------------------------------------------------------

# I have to process them all
# TRANSFORMATION : map function
# vvvvv
# Playing-with-my-dog-#dog-#fun-#dogLover
# I-love-my-dog-#dog-#dogLover
# I-love-my-cat-#cat-#catLover
# I-have-the-best-family-my-family-#family-#love
# Hate-school-@John-#school-#hate-#schoolIsAFuckingShit (18,000)
# vvvvv

# PACK all those tokens in a single list: FLATTEN
# ------------------------------------------------------
# Playing
# with
# my
# dog
# #dog
# #fun
# #dogLover
# I
# love
# my
# dog
# #dog
#.... (18,000 x 30 = 540,000)
# ------------------------------------------------------
# vvvv FILTER those tokens that are not hashtags
# #dog
# #fun
# #dogLover
# #dog
# #dogLover
# #cat
# #catLover
# #family
# #love
# #school
# #hate
# #schoolIsAFuckingShit

# vvvv SECOND FILTER: To remove those hashtags... that could be offensive

# #dog
# #fun
# #dogLover
# #DOG
# #dogLover
# #Cat
# #catLover
# #family
# #love
# #school
# #hate

# vvv Let's normalize the hashtags

# vvv CountByKey

# #dog 3
# #fun 1
# #dogLover 2
# #cat 1
# #catLover 1
# #family 1
# #love 1
# #school 1
# #hate 1
# --- At this moment NO TRANSOFRMATION HAS BEEN EXECUTED ---
# We have just annotated that those transformations have to be executed
# But they won't be executed until a reduce function is executed
# ---> Store that information in a Database

# When we use this way of creating software, we always apply a bunch of map functions... 
# one after the other... to transform the data... to filter the data... to normalize the data... to count the data... etc.
# collection > map > map > filter > map > map ... maybe 30 maps > map > reduce


my_list  = [1,2,3,4,5]

def is_odd(number):
    return number % 2 == 1

odd_numbers = filter(is_odd, my_list)
print(odd_numbers) # This is an unfinished job
                # The actual job... is executed when a reduce function is executed
                # That is something we have in the map-reduce model
                # map functions have a lazy behavior... they don't execute the transformation until it is needed
                # filter functions have a lazy behavior... they don't execute the filtering until it is needed
                # reduce functions have an eager behavior... they execute whatever they have to execute immediately

                # Once a stream of information is processed by a reduce function... it is consumed... and it is not available anymore

# Lambda expressions. What is that... 
# We have lambda expressions in python... and in many other programming languages.
# (JAVA, JS, C#, C++, etc)
# EXPRESSION? A piece of code that returns a value.
# So .. a lambda expression is a piece of code that returns a value.
# What is the value that a lambda expression returns? 
# A reference to an unnamed function defined within the expression itself.
my_function = lambda number: number * 2 # STATEMENT  (Python sentence)
              # This lambda expression is equivalent to the function twice


my_original_list = [1,2,3,4,5]

# Functional programming 
def twice(number):   # Defining a function... with its own behavior
    return number * 2
new_list = list(map(twice, my_original_list))                   # In new_list we have [2,4,6,8,10]

# Functional programming 
new_list = list(map( lambda number: number * 2 , my_original_list))

# I could have written the same code in imperative programming
new_list = []
for number in my_original_list:
    new_list.append(number * 2)