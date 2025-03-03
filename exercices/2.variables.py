# We said that we can create a reference to a value(data) stored in memory
# In order to do that we need to create a variable.
# In python we can easily create a variable by naming it and assigning a value to it.

name         = "Ivan"
age          = 48
phone        = "123456789"
zip_code     = "12345"
types_python = True


#name2        = "Brenda"
another_name  = "Brenda"
another_age   = 49
another_phone = "987654321"

number1 = 18
number2 = 3
number3 = number1 + number2 # This sentence is what we called an STATEMENT.
          #################
          # In this case, this statement contains an expression
          # An expresion `number1 + number2` is a piece of code that returns a value.

# We have already talk about DATA and VARIABLES. THIS IS PART of the python GRAMMAR: MORPHOLOGY
# In a language, morphology is the study of the structure of the tokens that make up the language.
# And actually the types of tokens that we can find in that language.

# In english, we have noums, verbs, pronouns, adjectives, adverbs, prepositions, conjunctions, and interjections.
# In python we have data, variables, operators, keywords, and punctuators.

# What is the equivalent of a noun in python?           DATA
# What is the equivalent in english of a variable?      PRONOUN

# The house is pretty.   HOUSE = NOUN
# It is big.             IT = PRONOUN... which refers to the house (NOUN)

# We have also said that a SENTENCE in english has an equivalent in python: STATEMENT
# En english we also combine nouns + adjectives to produce a noun phrase.
# An operator (such as the = sign) is a token that represents an action.
# In english what king of word do we use to represent an action? VERB
# Verbs in python are called operators and functions.

person = { "name": "Ivan", "age": 48, "phone": "123456789", "zip_code": "12345", "types_python": True }
person['name'] # That would point to the value "Ivan" in memory : RECOVER
person['age'] = 49 # That would point to the value 48 in memory : UPDATE

another_person = [ "Brenda", 49, "987654321", "12345", True ]
another_person[0]  # In python.. and actually in most programming languages, we start counting from 0.
another_person[1] = 50 # That would point to the value 49 in memory : UPDATE

an_extra_person = ( "Brenda", 49, "987654321", "12345", True )
an_extra_person[4]  # Recover whether the person likes python or not.
#an_extra_person[1] = 50 # I did told you that tuples are INMUTABLE... so this is going to raise an error.

# In python, STRINGS (Texts) are just a tuple of characters.

full_name = "Ivan Osuna"
another_variable_pointing_to_ivan = full_name
full_name[0] # This would point to the value "I" in memory : RECOVER
#full_name[0] = "J" # This would raise an error... because strings are INMUTABLE
full_name[0:4] # This would point to the value "Ivan" in memory : RECOVER
               # List/ tuple slicing is a way to recover a subset of values from a list/tuple.
               # In our case I did recover characters from the first one (position 0) to the fifth one (position 4) - NOT INCLUDED
full_name[5:]  # This would point to the value "Osuna" in memory : RECOVER
               # In this case I did recover characters from the sixth one (position 5) to the end of the string.
full_name[:4]  # This would point to the value "Ivan" in memory : RECOVER
               # In this case I did recover characters from the first one (position 0) to the fifth one (position 4) - NOT INCLUDED               
full_name[-1]  # This would point to the value "a"... the last value... Value at position 1, counting from the end of the string.
               # NOTE... when we count from the end of the string, we start counting from 1.
full_name[-5]  # This would point to the value "O"... the fifth value from the end of the string.
full_name[-5:] # This would point to the value "Osuna" in memory : RECOVER

full_name = "Dave Root" # This is not going to update the previous tuple
                        # This is going to create a new tuple in memory (is created in a new location in memory)
                        # The previous one is gonna be marked as garbage and it may will be collected by the garbage collector (o not).

# In this case, full_name points to "Dave Root" in memory.
# another_variable_pointing_to_ivan still points to "Ivan Osuna" in memory.

# This way of recovering values from a string is actually inherited from the way we recover values from a list or a tuple.

my_tuple = (1, 2, 3, 4, 5)
my_tuple[0] # This would point to the value 1 in memory : RECOVER
my_tuple[-1] # This would point to the last value 5 in memory : RECOVER
my_tuple[1:4] # This would point to the values 2, 3, 4 in memory : RECOVER
my_tuple[-3:] # This would point to the values 3, 4, 5 in memory : RECOVER