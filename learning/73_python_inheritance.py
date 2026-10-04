# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.


class a:                                    # parent class
    x = "Tom"
class b(a):                                 # child class
    def b(self):
    	print(self.x)
r = b()
r.b()

# Create a Parent Class
class Animal:                               # parent class
    def __init__(self, name):
        self.name = name
    def info(self):
        print("Animal name:", self.name)    
class dog(Animal):                          # child class inherits from parent class (Animal)
    def sound(self):
        print(self.name, "says woof!")
# Usage
a = dog("Buddy")
a.info()                                    # inherit method
a.sound()                                   # child method


# __init__() function
# The __init__() function is called automatically every time the class is being used to create a new object.
# When add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# The child's __init__() function overrides the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
class Car:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
    def ex(self):
        print("This car is", self.brand, self.name)
class Model(Car):
    def __init__(self, brand, name):
        Car.__init__(self, brand, name)
x = Model("Toyota", "camry")
x.ex()


# super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent
# By using the super() function, doesn't need to use the name of the parent element, 
# it will automatically inherit the methods and properties from its parent.
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def ex(self):
        print("My name is: ", self.fname, self.lname)
class Identity(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)            # Use super() function it doesnt need 'self'
x = Model("Riktam", "Sarkar")
x.ex()


# Add properties
class bike:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
    def ex(self):
        print(self.brand, self.name)
class Model(bike):
    def __init__(self, brand, name):
        super().__init__(brand, name)
        self.year = 2024
a = Model("Ducati", "V4")
print(a.year)               #here 'Print' is only print the added element 

#Add Methods
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("Myself", self.firstname, self.lastname, "and my birth date", self.graduationyear)
x = Student("Riktam", "Sarkar", 2002)
x.welcome()


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        # Call the parent class constructor
        super().__init__(brand, model) 
        # Add a unique child attribute
        self.battery_capacity = battery_capacity 

my_ev = ElectricCar("Tesla", "Model 3", "75 kWh")
print(my_ev.brand)            # Tesla (inherited)
print(my_ev.battery_capacity) # 75 kWh (child specific)
