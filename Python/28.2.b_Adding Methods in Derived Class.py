# Adding Methods in a Derived Class
# A child class inherits all methods from its parent class.
# However, you can also define new, unique methods inside the child class 
# that the parent class does not have.

class Person:                                   # parent class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):                        # parent method
        print(self.firstname, self.lastname)

class Student(Person):                          # child class inherits from parent
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)          # keep parent properties
        self.graduationyear = year              # add child property
        
    def welcome(self):                          # add unique child method
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# Usage
x = Student("Riktam", "Sarkar", 2002)

x.printname()                                   # calls the inherited parent method
x.welcome()                                     # calls the newly added child method