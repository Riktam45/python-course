# Python *args and **kwargs
# By default, a function must be called with the correct number of arguments.
# However, sometimes you may not know how many arguments that will be passed into your function.
# *args and **kwargs allow functions to accept a unknown number of arguments.

# Arbitrary Arguments - *args
# if you do not know how many arguments will be passed into your function, add a * before the parameter name.

def multiply_all(*args):
    result = 1
    for number in args:
        result *= number
    return result
print(multiply_all(2,3,4))


# The *args parameter allows a function to accept any number of positional arguments.
def child(*args):
    print("The first argument is :", (args[0]))
    print("The second argument is :", (args[1]))
    print("The third argument is :", (args[2]))
child("sona","pona","mona")

# A function that calculates the sum of any number of values
def _math_(*numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(_math_(123,987))
print(_math_(2134, 134))
print(_math_(378645,837546))    

# Arbitrary Keyword Arguments - **kwargs
# The **kwargs parameter allows a function to accept any number of keyword arguments.
# If you do not know how many keyword arguments will be passed into your function, 
# add two asterisks ** before the parameter name.
def func(**cars):
    print(cars)
func(brand = "toyota", model = "supra", edition = "3rd gen")

# Combining *args and **kwargs
# we can use both *args and **kwargs in the same function.
# The order must be:
# regular parameters
# *args
# **kwargs
def _func_(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)
_func_("User Info", "Riktam", "Sarkar", age = 23, city = "Kolkata")