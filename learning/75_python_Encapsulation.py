# Python Encapsulation
# Encapsulation is about protecting data inside a class.
# It means keeping data (properties) and methods together in a class, 
# while controlling how the data can be accessed from outside the class.
# This prevents accidental changes to data and hides the internal details of how class works.

# Implementing Encapsulation
# Get Private Property Value
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age    # Creates a private instance variable named __age. The double underscore (__) triggers name mangling in Python, making it harder to access this variable directly from outside the class.
    def get_age(self):
        return self.name, self.__age
p1 = Person("Riktam", 23)
print(p1.get_age())

# Set Private Property Value
# To modify a private property, you can create a setter method
# The setter method can also validate the value before setting it
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")
p1 = Person("Riktam", 23)
print(p1.get_age())
p1.set_age(26)
print(p1.get_age())
    
# Protected Properties
class Car:
    def __init__(self, brand):
        self._brand = brand     # Protected property
c1 = Car("Mazda")
print(c1._brand)                # Can access, but shouldn't


# All the properties(public, private, protected)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner            # Public attribute
        self._account_type = "Savings" # Protected attribute (convention)
        self.__balance = balance      # Private attribute (triggers name mangling)

    # Getter method to safely access private data
    def get_balance(self):
        return self.__balance

    # Setter method to safely modify private data with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

# Usage
account = BankAccount("Alice", 1000)

print(account.owner)           # Output: Alice (Accessible)
print(account._account_type)   # Output: Savings (Accessible, but discouraged)

# print(account.__balance)     # Throws AttributeError (Protected by name mangling)

print(account.get_balance())   # Output: 1000 (Proper access via Getter)
account.deposit(500)           # Modifies state via controlled Setter method


# Name Mangling
# Name mangling is how Python implements private properties and methods.
# When you use double underscores __, Python automatically renames it internally by adding _ClassName in front.
# For example, __age becomes _Person__age.
# Name mangling is Python's internal process of altering the name of a class attribute prefixed with a double underscore (like __variable) into _ClassName__variable to prevent naming conflicts during inheritance.