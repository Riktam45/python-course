# Recursion
# Recursion is when a function calls itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. 
# This has the benefit of meaning that you can loop through data to reach a result.
"""The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, 
or one that uses excess amounts of memory or processor power. 
However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming."""

def countdown(n):
    if n <= 0:
        print("Done")
    else:
        print(n)
        countdown(n-1)  # That line makes it recursive because the function is using its own name to call itself from within its own body.
countdown(5)

# Base Case and Recursive Case
# Every recursive function must have two parts:
# A base case - A condition that stops the recursion
# A recursive case - The function calling itself with a modified argument
# Without a base case, the function would call itself forever, causing a stack overflow error.

def factorial(n):
    #Base case
    if n == 0 or n == 1:
        return 1
    # Recursive cse
    else:
        return n * factorial(n - 1)
print(factorial(5))

# Fibonacci Sequence
# he Fibonacci sequence is a classic example where each number is the sum of the two preceding ones. 
# The sequence starts with 0 and 1:
# 0, 1, 1, 2, 3, 5, 8, 13, ...
# The sequence continues indefinitely, with each number being the sum of the two preceding ones.

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))