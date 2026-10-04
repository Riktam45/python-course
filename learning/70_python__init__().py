# The __init__() Method
# All classes have a built-in method called __init__(), 
# which is always executed when the class is being initiated.
# The __init__() method is used to assign values to object properties, 
# or to perform operations that are necessary when the object is being created.

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = person("Riktam", 23)
print(p1)   # When you run print(p1) without telling Python how to display the object, Python defaults to showing you where that object lives in your computer's RAM (memory)
print(p1.name)
print(p1.age)

# In Python, self is a convention used as the first parameter in instance methods of a class. It represents the specific object (instance) that you are currently working with.
# 1. What is self?
# When you create multiple objects from a single class (like p1 = person("Riktam", 23) and p2 = person("Amit", 25)), Python needs a way to know which object's data you want to access or modify.
# self is simply a placeholder name for "the current object".
# 2. Why do we need self?
# Reason A: To tie data to a specific object
class person:
  def __init__(self, name, age):
    self.name = name  # Binds 'name' to the specific object
    self.age = age  # Binds 'age' to the specific object

# Reason B: To let objects interact with their own methods
# When a method (like a function inside a class) needs to use an object's data, it uses self to reach it:
class person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def introduce(self):
    # 'self' tells Python: "Get the name and age of *this* specific object"
    return f"Hi, I am {self.name} and I am {self.age} years old."
p1 = person1("Riktam", 23)
p2 = person1("Sarkar", 25)
print(p1.introduce())  # Output: Hi, I am Riktam and I am 23 years old.
print(p2.introduce())  # Output: Hi, I am Sarkar and I am 25 years old.

# Multiple Parameters
class cars:
   def __init__(self, brand, model, color, year):
      self.brand = brand
      self.model = model
      self.color = color
      self.year = year
cl = cars("Lamborghini", "Huracan", "Red", 2022)
print(cl.brand)
print(cl.model)
print(cl.color)
print(cl.year)


# Create a class called Dog
# Add an __init__ method with parameters name and age, and store them as properties using self
# Add a method called bark that prints the dog's name followed by " says Woof!"
# Create an object d1 of the Dog class with name "Buddy" and age 3
# Call the bark method on d1

class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def bark(self):
		return f"{self.name} Says Woof! and age {self.age}"
d1 = Dog("Buddy", 3)
print(d1.bark())

class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def greet(self):
    print("Hello, my name is " + self.name)
p1 = Person1("Riktam", 23)
p1.greet()

# It does not have to be named self, you can call it whatever you like, 
# but it has to be the first parameter of any method in the class:
class bike:
    def __init__(myobject, name):
        myobject.name = name
    def ano(abc):
        return "This is " + abc.name
bi_ke = bike("R1")
print(bi_ke.ano())
# While you can use a different name, it is strongly recommended to use self as it is the convention in Python and makes your code more readable to others.

