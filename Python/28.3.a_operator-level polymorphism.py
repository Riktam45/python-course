# Operator Polymorphism
# Operator polymorphism means the same operator can have different behaviors depending on the data type or object.
# The most common example is the '+' operator, which performs addition for numbers, but concatenation for strings.

# Built-in Operator Polymorphism
a = 10
b = 20
print(a + b)                                    # '+' acts as Addition: outputs 30

c = "Hello "
d = "World"
print(c + d)                                    # '+' acts as Concatenation: outputs "Hello World"


# Operator Overloading in Custom Classes
# We can define how standard operators work for our own classes using "magic methods" like __add__().
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):                   # Overloading the '+' operator for the Point class
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

# Usage
p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2                                    # This calls the __add__ method we defined
print(p3.x, p3.y)                               # outputs 4 6