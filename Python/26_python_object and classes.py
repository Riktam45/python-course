# Class
# A class is a user-defined blueprint or prototype from which objects are created. 
# It serves as a template that defines a set of attributes (variables) and methods (functions) that the created objects will possess.

# creating a class
# To create a class, use the keyword class
class Myclass:
    x = 5       # class attribute
print(Myclass)

# Object
# An object is an instance of a class. When a class is defined, 
# no memory is allocated until an object of that class is instantiated. 
# Each object can contain unique data while sharing the behavior defined by its class.

# creating a object
# Create an object named p1, and print the value of x
class Myclass:
    x = 5
p1 = Myclass()
print(p1.x)

# Delete Objects
#del p1      # this shows error because the p1 object is no longer exists
#print(p1)

# Multiple Objects
class dog:
    sound = "bark"
p1 = dog()
p2 = dog()
p3 = dog()
print(p1.sound)
print(p2.sound)
print(p3.sound)

