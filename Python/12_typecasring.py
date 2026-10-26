"""In Python there are different data types, such as numbers, sequences, mappings etc. 
There may be a situation where, you have the available data of one type but you want to use it in another form. 
For example, the user has input a string but you want to use it as a number. 
Python's type casting mechanism let you do that."""

#Python supports two types of casting − implicit(automatic) and explicit(manual).

# 1. Implicit Casting
# Python automatically converts one data type to another to prevent data loss. 
# This usually happens when you perform arithmetic operations between different numeric types, 
# such as adding an integer to a float.

int_val = 5       # int   
float_val = 6.0     # float
result_val = int_val + float_val
print(result_val)    # in here a is int and b is float, but the result is float. this is implicit casting.
print(type(result_val))

# True is equal to 1, and False is equal to 0.
a1 = True
b1 = 34.56
c1 = a1 + b1
print(c1)    #in here a1 is bool and b1 is float, but the result is float. this is implicit casting.

# 2. Explicit Casting(Manual)
# Explicit type casting is done manually by the programmer using Python's built-in constructor functions.

# Function	    Description	                                                          Example
# int()	        Converts a value to an integer. Truncates decimals from floats.	      int(5.9) → 5 
#                                                                                     int("10") → 10
# float()	    Converts a value to a floating-point number.	                      float(3) → 3.0
#                                                                                     float("4.5") → 4.5
# str()	        Converts a value into a string representation.	                      str(100) → "100"
#                                                                                     str(True) → "True"
# bool()	    Converts a value to a boolean (True or False).	                      bool(0) → False
#                                                                                     bool("Hello") → True

# i. Converting String to Numeric Types (Handling User Input)
# When accepting data using input(), Python reads everything as a string. To do math, you must cast it.
age_str = 23            # User input comes as a string
age = int(age_str)      # Explicitly cast to integer
next_year = age_str + 1     # Now mathematical operations are allowed
print(next_year)

# ii. Converting Float to Integer (Data Loss)
# Casting a float to an int chops off the decimal part rather than rounding to the nearest whole number.
number = 34.97
num_to_int = int(number)
print(num_to_int)

# iii. Combining Numbers and Strings
# Python will throw a TypeError if you try to add or concatenate a string and a number without casting.
num = 23
text = "I am Riktam and I am " + str(num) + " years old" # spce after and before two separeted "" for space in between in output
print(text)

# 3. Collection Type Casting
# You can also explicitly cast between sequence types using data structure constructors:
# list(): Converts a tuple or string into a list → list((1, 2, 3)) becomes [1, 2, 3]
# tuple(): Converts a list or string into a tuple → tuple([1, 2]) becomes (1, 2)
# set(): Converts a list into a set (removing duplicate items) → set([1, 2, 2, 3]) becomes {1, 2, 3}

