"""In Python there are different data types, such as numbers, sequences, mappings etc. 
There may be a situation where, you have the available data of one type but you want to use it in another form. 
For example, the user has input a string but you want to use it as a number. 
Python's type casting mechanism let you do that."""

#Python supports two types of casting − implicit and explicit.
#Implicit Casting
a = 5
b = 6.0
c = a + b
print(c)    #in here a is int and b is float, but the result is float. this is implicit casting.

# True is equal to 1, and False is equal to 0.
a1 = True
b1 = 34.56
c1 = a1 + b1
print(c1)    #in here a1 is bool and b1 is float, but the result is float. this is implicit casting.