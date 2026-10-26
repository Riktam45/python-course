# Python Variables
# Variables are containers for storing data values.
x = 5
y = "Name"
print(x)
print(y)

#  specify the data type of a variable, this can be done with casting.
x1 = str("madh")
y1 = int(3)
z1 = float(3)
print(x1)
print(y1)
print(z1)

# the data type of a variable with the type() function
x2 = 5
y2 = "NAME"
print(type(x2))
print(type(y2))

# Multiple variables can be assigned in one line
a, b, c = "object1", "object2", "object3"
print(a)
print(b)
print(c)

# And you can assign the same value to multiple variables in one line
a1 = b1 = c1 = "Object_same"
print(a1)
print(b1)
print(c1)

# Unpack a collection
# If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables.
# This is called unpacking.
fruits = ["Orange", "Apple", "Cherry"]
j, k, l = fruits
print(j)
print(k)
print(l)