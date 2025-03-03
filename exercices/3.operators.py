# Operators allow us to perform operations on variables and values.
# What kind of operators do we have in python?
# They depend on the type of data that we are working with.

# Operators related to numbers:

# +  Addition
# -  Subtraction
# *  Multiplication
# /  Division
# // Integer division (floor division)
# %  Modulus (remainder of the integer division)
# ** Exponentiation

2 + 3      # That would return 5
2 - 3      # That would return -1
2 * 3      # That would return 6
10 / 3     # That would return 3.3333333333333335
10 // 3    # That would return 3
10 % 3     # That would return 1
10 ** 3    # That would return 1000
             #          10 | 3
             #           9 +------
             #         ---   3 <<<< The result is 3
             #           1 <<< The remainder is 1

# Operators have a precedence order.
# For example the multiplication operator has a higher precedence than the addition operator.
# So in the following expression: 2 + 3 * 4 = 14
# For sure we can group operations using parentheses, and doing that we can change the precedence order.
# For example:
(2 + 3) * 4 # That would return 20

number1 = 18
number2 = 3
number3 = number1 + number2 
number4 = number1 - number2
number5 = number1 * number2 / number3

# Operators related to strings:

# Concatenation operator
"Hello " + "World" # That would return "Hello World"
# NOTE: At that point we would have in memory 3 strings: "Hello", "World", and "Hello World"

"hi" * 3 # That would return "hihihi"

# Operators related to booleans: We have 3:

value1 = True
value2 = False

# AND operator: Only returns True if both values are True
value1 and value2 # That would return False

# OR operator: Returns True if at least one of the values is True
value1 or value2 # That would return True

# NOT operator
not value1 # That would return False


# Comparison operators: When applied on 2 elements of same type, they return a boolean value.

value1 = 5
value2 = 10

value1 == value2 # That would return False
value1 != value2 # That would return True
value1 < value2  # That would return True
value1 <= value2 # That would return True
value1 > value2  # That would return False
value1 >= value2 # That would return False

value1 = "Hello"
value2 = "Bye" # The comparison is made by comparing the ASCII values of the characters.

value1 == value2 # That would return False
value1 != value2 # That would return True
value1 < value2  # That would return False
value1 <= value2 # That would return False
value1 > value2  # That would return True
value1 >= value2 # That would return True

# Assignment operators: They are used to assign values to variables.

value1 = 5

number = 7
number = number + 1 # That would return 8
# In other programming languages we could write number++; (C, JAVA, JS)
# COMMENT... thats the reason C++ is called C++... because it is an increment of C... 
# and C has the increment operator.
#                      C#... They called C sharp like that.. because is an incremnt to the previous language C++
#                      It was 2 increments  C++ 
#                                            ++
#number++ # In java, variable number would point to 9
# In python we don not have that operator... but we have something better... operational assignment operators.

number = 10
number += 1 # That would make number point to 11
number -= 1 # That would make number point to 10
number *= 2 # That would make number point to 20
number /= 2 # That would make number point to 10
number //= 3 # That would make number point to 3
number %= 2 # That would make number point to 1

# Collection operators: They are used to work with collections.

list = [1, 2, 3]
tuple = (1, 2, 3)

## In operator: It returns True if the value is found in the collection.

1 in list # That would return True
4 in tuple # That would return False

# Be careful.... The in operator is also used as part of the for loop.