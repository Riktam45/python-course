# Python Inner Classes
# An inner class is a class defined inside another class. The inner class can access the properties and methods of the outer class.
# Inner classes are useful for grouping classes that are only used in one place, making your code more organized.
class Outer:
    def __init__(self):
        self.name = "Outer class"
class Inner:
    def __init__(self):
        self.name = "Inner class"
s1 = Outer()
print(s1.name)

# Accessing Inner Class from the Outside
class Outer:
    def __init__(self):
        self.name = "Outer Class"
    class Inner:                        # the Inner class is inside the Outer class 
        def __init__(self):
            self.name = "Inner Class"
        def display(self):
            return self.name
s1 = Outer()
s2 = s1.Inner()
print(s2.display())

# Accessing Outer Class from Inner Class
class Outer:
  def __init__(self):
    self.name = "Emil"
  class Inner:
    def __init__(self, outer):
      self.outer = outer
    def display(self):
      print(f"Outer class name: {self.outer.name}")
x = Outer()
y = x.Inner(x)
y.display()


# Multiple Inner Classes
class Computer:
  def __init__(self):
    self.cpu = self.CPU()
    self.ram = self.RAM()
  class CPU:
    def process(self):
      print("Processing data...")
  class RAM:
    def store(self):
      print("Storing data...")
computer = Computer()
computer.cpu.process()
computer.ram.store()