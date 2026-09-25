# Lesson 4: Functions


# What is this topic?
# A function is a reusable block of code that performs a specific task.
# Functions help organize a program and prevent repeated code.


# Key vocabulary
# Function - a reusable block of code that performs a specific task.
# Parameter - a variable placed inside the function.
# Argument - the actual value given to a parameter.
# Return value - the result sent back by a function using return.


# My own example(s)

def calculate_total(price, quantity):
    total = price * quantity
    return total


price = 50
quantity = 3

result = calculate_total(price, quantity)

print("Total price:", result)


# A mistake I made
# One mistake I made was forgetting to use the return statement.
# I learned that return is needed when I want a function to send
# a result back to the part of the program that called it.
