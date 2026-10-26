# Python Functions

# def function_name(parameters):      ]
#   statements                        ] - function definition
#   return expression                 ]
# function_call(arguments)

# A function is a block of code which only runs when it is called.
# A function can return data as a result.
# A function helps avoiding code repetition.
def my_function():
    print("Hello!")
my_function()
my_function()
my_function()   # can call the function multiple time

# Function names follow the same rules as variable names in Python:
# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)

# With functions, you write the code once and reuse it:
def fahrenheit_to_celsius(fahrenheit):  #fahrenheit is parameters
    return (fahrenheit - 32) * 5 / 9    # The return keyword is used because it sends the result of the calculation back to the place where the function was called
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# The direct answer is: print() displays text on your screen, 
# while return hands a value back to your code so you can use it for other tasks (like math or saving data)

# Return Values
# Functions can send data back to the code that called them using the return statement.
# When a function reaches a return statement, it stops executing and sends the result back:
def cars():
    return "Its a car"
x = cars()
print(x)

def my_function1(x, y):
  return x + y
result = my_function1(5, 3)
print(result)

# Returning Different Data Types
# Functions can return any data type, including lists, tuples, dictionaries, and more.
# A function that returns a list:
def my_function2():
  return ["apple", "banana", "cherry"]
fruits = my_function2()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# A function that returns a tuple:

def my_function3():
  return (10, 20)
x, y = my_function3()
print("x:", x)
print("y:", y)