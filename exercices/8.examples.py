
# Create a function called maximum that return the maximum value of 2 numbers.
# If those numbers are equal, the function should return any of them.

def maximum(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2

def maximum(number1, number2):
    if number1 > number2:
        return number1 # This line stops the execution of the function and returns the value of number1
    return number2

def maximum(number1, number2):
    return number1 if number1 > number2 else number2

print(maximum(5, 10)) # This would print 10
print(maximum(10, 5)) # This would print 10
print(maximum(10, 10)) # This would print 10
print(maximum(-5, 1)) # This would print 1

# Create a function called maximum_of_three that return the maximum value of 3 numbers.
# If those numbers are equal, the function should return any of them.

def maximum_of_three(number1, number2, number3):
    return maximum(maximum(number1, number2), number3) # This is clean, elegant and easy to read

