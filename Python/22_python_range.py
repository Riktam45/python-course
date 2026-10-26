# Python range
# he built-in range() function returns an immutable sequence of numbers, 
# commonly used for looping a specific number of times.
# This set of numbers has its own data type called range.

# Creating ranges
# The range() function can be called with 1, 2, or 3 arguments, using this syntax:
# range(start, stop, step)

# Range with one argument
# If the range function is called with only one argument, the argument represents the stop value.
# The start argument is optional, and if not provided, it defaults to 0.

x = range(10)
print(x)
#convert to list to display the content of x:
print(list(x))


# Call range() With Two Arguments
# If the range function is called with two arguments, the first argument represents the start value, and the second argument represents the stop value.
# range(3, 10) returns a sequence of each number from 3 to 9

x1 = range(3, 10)
print(x1)
#convert to list to display the content of x:
print(list(x1))

# Call range() With Three Arguments
# If the range function is called with three arguments, the third argument represents the step value.
# The step value means the difference between each number in the sequence. It is optional, and if not provided, it defaults to 1.
# range(3, 10, 2) returns a sequence of each number from 3 to 9, with a step of 2:

x2 = range(3, 10, 2)
print(x2)
#convert to list to display the content of x:
print(list(x2))

# Ranges are often used in for loops to iterate over a sequence of numbers
for i in range(6):
    print(i)