# This is a simple program to demonstrate type conversion in Python.
x = 23
y = 34.56
z = 1j

a = float(x)    #convert the integer value of x to a floating point value
b = int(y)      #convert the floating point value of y to an integer value
c = int(x)      #convert the integer value of x to an integer value

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))