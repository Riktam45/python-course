# Function Polymorphism
# Function polymorphism means a single function can accept different types of arguments and process them accordingly.
# There are built-in polymorphic functions (like len()) and we can also create our own.

# Built-in Function Polymorphism
x = "Hello World"
y = [10, 20, 30, 40]

print(len(x))                                   # len() works on a string: outputs 11
print(len(y))                                   # len() works on a list: outputs 4


# User-Defined Function Polymorphism
# We can write a standalone function that accepts any object, 
# and it will work as long as the object has the method we are calling.
class Tomato:
    def group(self):
        print("I am a vegetable")

class Apple:
    def group(self):
        print("I am a fruit")

def check_group(obj):                           # This standalone function is polymorphic
    obj.group()                                 # It calls group() regardless of whether obj is Tomato or Apple

# Usage
t1 = Tomato()
a1 = Apple()

check_group(t1)                                 # outputs "I am a vegetable"
check_group(a1)                                 # outputs "I am a fruit"