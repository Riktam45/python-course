# Python Polymorphism
# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.


# Class Polymorphism
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def x(self):
        print("Drive")
class Boat:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
    def x(self):
        print("Sail")
class Plane:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
    def x(self):
        print("Fly")
vehicle1 = Car("Chevy","Impala")
vehicle2 = Boat("Ibiza", "Touring 20")
vehicle3 = Plane("Boeing", "A370")

for ex in (vehicle1, vehicle2, vehicle3):
    ex.x()

# Inheritance Class Polymorphism
# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Move!")
class Car(Vehicle):
  pass
class Boat(Vehicle):
  def move(self):
    print("Sail!")
class Plane(Vehicle):
  def move(self):
    print("Fly!")
car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object
for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()


# Inside the editor, complete the following steps:
# Create a class Cat with a method sound that prints "Meow"
# Create a class Fox with a method sound that prints "Wa-pa-pa-pa-pa-pow!"
# Create objects c1 = Cat() and f1 = Fox()
# Call sound() on both objects
class Cat:
	def sound(self):
		print("Meow")
class Fox:
	def sound(self):
		print("Wa-pa-pa-pa-pa-pow!")
c1 = Cat()
f1 = Fox()
for ex in (c1, f1):
	ex.sound()
